import urllib.parse
import requests
import json
import sys
import os
import sqlite3
import pandas as pd
import urllib.parse as par
import copy
from time import sleep, perf_counter
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from boilerpy3 import extractors
from bs4 import BeautifulSoup

from concurrent.futures import ProcessPoolExecutor, as_completed

# Child class to apply fix to boilerpy function.
# Use this instead of extractors.DefaultExtractor.
class custom_boilerpy3(extractors.DefaultExtractor):
    def read_from_url(self, url: str) -> str:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            with urllib.request.urlopen(req, timeout = 10) as url_obj:
                text = url_obj.read()
                encoding = self.get_url_encoding(url_obj)
        except:
            print('Timeout for', url)
            return 'NIL'
        try:
            text = text.decode(encoding)
        except UnicodeDecodeError:
            pass
        return text

class History:

    # Get address of user chrome browser history
    data_path = os.path.expanduser('~')+r"\AppData\Local\Google\Chrome\User Data\Default"
    hist_path = os.path.join(data_path, 'History')
    searchSiteList = [
        "www.youtube.com",
        "search.yahoo.com",
        "sg.search.yahoo.com",
        "www.google.com"
    ]

    # Change sensitivity parameter to adjust how many terms are returned.
    def __init__(self, sensitivity, chromeHistoryDir = None, sampleFile = None):
        self.sensitivity = sensitivity
        if chromeHistoryDir != None:
            self.data_path = chromeHistoryDir
            if sampleFile != None:
                self.hist_path = os.path.join(self.data_path, sampleFile)
            else:
                self.hist_path = os.path.join(self.data_path, 'History')
        self.getHistory()

    # Returns your chrome history as a list.
    def getHistory(self):
        try:
            c = sqlite3.connect(self.hist_path)
            cursor = c.cursor()
            select_statement = "SELECT urls.url, urls.visit_count FROM urls;"
            cursor.execute(select_statement)
            results = cursor.fetchall()
        except:
            raise ImportError("There was an error collecting your browser history. PLease ensure that your Chrome broswer is closed before trying again.")

        self.sites = []
        self.searches = []
        self.youtube = []
        series = {}

        for entry in results:
            urlParse = par.urlparse(entry[0])
            series['netloc'] = urlParse.netloc
            series['visits'] = entry[1]
            series['scheme'] = urlParse.scheme
            series['path'] = urlParse.path
            series['params'] = urlParse.params
            series['query'] = urlParse.query
            series['fragment'] = urlParse.fragment
            if series['visits'] <= self.sensitivity:
                continue
            if series['netloc'] in self.searchSiteList:
                if series['netloc'] == "www.google.com" and series['query'][:2] == 'q=':
                    tempString = series['query'][2:series['query'].find('&')]
                    self.searches += [copy.copy(tempString.split('+'))]
                if series['netloc'] == "www.youtube.com" and series['query'][:13] == 'search_query=':
                    tempString = series['query'][13:]
                    self.youtube += [copy.copy(tempString.split('+'))]
                if series['netloc'] == "search.yahoo.com" or series['netloc'] == "sg.search.yahoo.com" and series['query'][:2] == 'p=':
                    tempString = series['query'][2:series['query'].find('&')]
                    self.searches += [copy.copy(tempString.split('+'))]
            else:
                self.sites += [copy.copy(series)]

class TermSearch:

    jsonDir = 'searchResult.json'

    URL =  "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/WebSearchAPI"
    DDGURL = 'https://duckduckgo.com/html/?q='
    yahooURL1 = r'https://search.yahoo.com/search?p='
    yahooURL2 = r'&toggle=1&ei=UTF-8'

    # Unique API key
    headers = {"x-rapidapi-host": "contextualwebsearch-websearch-v1.p.rapidapi.com",
	    "x-rapidapi-key": "8fff77902emsh00cf565853c31afp1c8e5fjsnd045cae7f04b"}

    # User agent headers for use with DuckDuckGo get request
    DDGheaders = {
    'User-Agent': 'Mozilla/5.0',
    'From': 'fake@domain.com'}

    param = {
        "autoCorrect": "true",
	    "pageNumber": "1",
	    "pageSize": "1",
	    "q": "Taylor Swift",
	    "safeSearch": "false"
        }

    # Uses Yahoo! search engine.
    def getSearchResultV3(self,query):
        searchTerm = ''
        index = 0
        for word in query:
            index += 1
            searchTerm += word
            if index != len(query):
                searchTerm += '+'
        yahooURL = self.yahooURL1 + searchTerm + self.yahooURL2
        res = requests.get(yahooURL)
        text = res.text

        soup = BeautifulSoup(text, features = 'lxml')

        for item in soup.find_all(referrerpolicy='origin'):
            sleep(0.1)
            if item.get('href') == None:
                print("An error occured with Yahoo parsing, None type was returned.")
            else:
               print(item.get('href'))
            return item.get('href')
        

            

    # Returns a list of web search results from an input list of search queries.
    # Each search query must be a list of words, as output by the History class.
    # Uses DuckDuckGo search engine for (theoretically) unlimited searches.
    def getSearchResultV2(self, query, save_file = True):
        searchTerm = ''
        for word in query:
            searchTerm += (word + '_')
        searchTerm = searchTerm[:-1]
        response = requests.get(self.DDGURL + searchTerm, headers = self.DDGheaders)
        if response.status_code != 200:
            print('Error %d occured, retrying...' % (response.status_code))
            response = requests.get(self.DDGURL + searchTerm, headers = self.DDGheaders)
            if response.status_code != 200:
                print('Retry failed.')
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a', attrs={'class':'result__a'}, href=True)

        # Terminates after first URL, but code is in place for collecting >1 per search query.
        count = 0
        result = ''
        for link in results:
            if count == 1: break
            try:
                url = link['href']
                o = urllib.parse.urlparse(url)
                d = urllib.parse.parse_qs(o.query)
                result += d['uddg'][0]
                count += 1
            except:
                pass

        #sleep(1)
        #print("Search completed with success rate of %.2f%%." % (len(resultList)/len(queryList)*100))
        #if save_file:
        #    with open(self.jsonDir, 'w') as file:
        #        json.dump(resultList, file, indent = 4, separators = (',', ': '))
        #        print("Json file saved under", self.jsonDir)

        return result

    # Extracts text from a SINGLE given URL webpage.
    def getSiteText(self, URL):
        # Remember to use custom_boilerpy3 here to apply the fix!
        extractor = custom_boilerpy3()
        content = extractor.get_content_from_url(URL)
        return content

    # Search the web using ContextualWeb search; limit to 10k queries monthly
    # DEPRECATED, use V2 instead
    def _getSearchResult(self, termList, save_file = True):

        print(len(termList), 'entries to be searched...')
        runningJson = []
        for entry in termList:
            searchTerm = ''
            for word in entry:
                searchTerm += (word + ' ')
            self.param['q'] = searchTerm
            response = requests.get(self.URL, params = self.param, headers = self.headers)

            if response.status_code == 200:
                print("Request successful")
            else:
                print("Response failed with error code", response.status_code)
            runningJson += [response.json()]
        if save_file:
            with open(self.jsonDir, 'w') as file:
                json.dump(runningJson, file, indent = 4, separators = (',', ': '))

class TextFeatureExtractor:

    # Class takes a text corpus list as input, as output by Termsearch.getSiteText()
    def __init__(self, corpus,
                vectorizer = CountVectorizer(token_pattern = r'(?u)\b[a-zA-Z]\w+\b', analyzer = 'word', stop_words = 'english'),
                transformer = TfidfTransformer(smooth_idf = False),
                transformer_tfn = TfidfTransformer(norm = 'l1', use_idf = False, smooth_idf = False),
                parent = True):

        self.corpus = corpus
        self.vectorizer = vectorizer
        self.transformer = transformer
        self.transformer_tfn = transformer_tfn
        if parent == True:
            self._getFeatures()
        else:
            self._getFeatures_noFit()
        self._getdf()
        self._getdf_tf()
        self._getdf_tfn()

    # Get list of word occurances for each document.
    def getWordCount(self, word):
        wordPos = self.getFeatureNames().index(word)
        countList = []
        for doc in self.getCountArray():
            countList += [doc[wordPos]]
        return countList

    # Private methods

    # Finds the feature list, as well as the tfidf matrix for the feature list.
    # Parent getFeature function. For first call of TextFeatureExtractor. Executes on object initiation.
    def _getFeatures(self):
        self.featureCount = self.vectorizer.fit_transform(self.corpus)
        self.tfidf = self.transformer.fit_transform(self.featureCount)
        self.tfn = self.transformer_tfn.fit_transform(self.featureCount)

    # Finds the feature list, as well as the tfidf matrix for the feature list. Does not have fit function as a child extractor.
    # Child getFeature function. Fit will be obtained from a parent call of TextFeatureExtractor. Executes on object initiation.
    def _getFeatures_noFit(self):
        self.featureCount = self.vectorizer.transform(self.corpus)
        self.tfidf = self.transformer.transform(self.featureCount)
        self.tfn = self.transformer_tfn.transform(self.featureCount)

    # Populate a pandas dataframe with tfidf matrix. Executes on object initiation.
    def _getdf(self):
        self.df = pd.DataFrame(self.tfidf.toarray())
        self.df.columns = self.getFeatureNames()

    # Populate a pandas dataframe with tf matrix. Executes on object initiation.
    def _getdf_tf(self):
        self.df_tf = pd.DataFrame(self.featureCount.toarray())
        self.df_tf.columns = self.getFeatureNames()

    # Populate a pandas dataframe with NORMALIZED tf matrix. Executes on object initiation.
    def _getdf_tfn(self):
        self.df_tfn = pd.DataFrame(self.tfn.toarray())
        self.df_tfn.columns = self.getFeatureNames()

    # Get numpy array of word counts within the corpus.
    def getCountArray(self):
        return self.featureCount.toarray()

    # Get list of individual features within the corpus.
    def getFeatureNames(self):
        return self.vectorizer.get_feature_names()

def parallelize_search(searchCount, query):
        print("Search", searchCount, "started for terms", query)
        searchEngine = TermSearch()
        url = searchEngine.getSearchResultV2(query)
        searchCount += 1
        print("Search", searchCount, "completed for terms", query)

        # Search for site texts
        try:
            siteText = searchEngine.getSiteText(url)
            print("Search", searchCount, "Text collected for terms", query)
            return siteText
        except:
            print("ERROR: Search", searchCount, "Error visiting URL for term ", query, "skipping...")



if __name__ == '__main__':

    start_time = perf_counter()
    # Set working directory to always be current script folder
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    os.chdir(ROOT_PATH)

    hist = History(sensitivity = 10)
    print(len(hist.searches), 'search terms returned')
    print()

    textList = []
    with ProcessPoolExecutor() as executor:
        results = [executor.submit(parallelize_search, searchCount, query) for searchCount, query in zip(range(len(hist.searches)), hist.searches)]
        for f in as_completed(results):
            if f.result() != None:
                textList += [f.result()]

    sleep(0.5)
    extractor = TextFeatureExtractor(textList)
    end_time = perf_counter()

    print("Time taken for search is:", end_time-start_time)
