from boilerpy3 import extractors
import pandas as pd
import os
import json
import sys
from collections import Counter
from pprint import pprint

dir_main = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(dir_main, "google_custom_search"))
import custom_search_V3 as csV3

filename_dataset = "dataset.json"
filename_URLcsv = "WordList_Training.csv"
cur_URL_list = []

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
os.chdir(ROOT_PATH)

website_df = pd.read_csv(filename_URLcsv)

try:
    with open(filename_dataset, "r") as file:
        print ("File exist")
        if os.path.getsize(filename_dataset) != 0:
            data = json.load(file)
            for item in data: cur_URL_list.append(item["URL"])
        else: data = []
except :
    print ("File not exist, creating file...")
    with open(filename_dataset, "w"): pass
    data = []

searchEngine = csV3.TermSearch()
url_dict = []

count = 1
for index, row in website_df.iterrows():
    website = row["URL"]
    category = row["Category"]

    if website in cur_URL_list:
        print("Repeated URL found for", website)
        continue

    print("Trying to collect words from ", website)
    content = ""

    try:
        textList = [searchEngine.getSiteText(website)]
        print("Text collected for ", count, website)
        count += 1
        url_dict.append({"URL": website, "Category": category, "wordList": textList})
    except:
        print("Error visiting URL, skipping...")

    # for item in url_dict: print(item["URL"])

with open(filename_dataset, "r+") as file:
    for item in url_dict: data.append(item)
    json.dump(data, file, indent = 4)

with open(filename_dataset, "r") as file:
    if os.path.getsize(filename_dataset) != 0:
        data = json.load(file)
    else: data = []

c = Counter(website["Category"] for website in data)
pprint(c)
print("Total websites: ", sum(c.values()))
