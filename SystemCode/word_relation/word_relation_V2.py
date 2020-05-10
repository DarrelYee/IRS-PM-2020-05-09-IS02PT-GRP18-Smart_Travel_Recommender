# This module has 2 classes
# WordRelation class: generates the model using Naive Bayes superviser learning model and includes calculating accuracy of the model_selection
# PredictCat class: Takes in the model and the tfidf to be predicted and predicts the categories for the parsed tfidf elements
#
# Running this file alone is able to generate the average accuracy of the model across 50 random states of training/test data sets using 80/20 split
# Model uses default random_state = 24 since it yields the highest accuracy

import sys
import os
import json
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn import metrics
from collections import Counter

dir_main = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(dir_main, "custom_search"))

import custom_search_V3 as csV3

#ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
#os.chdir(ROOT_PATH)

class WordRelation:

    # Class to build model to corelate websites to categories. Takes in dataset.json as training set for building model
    def __init__(self, state = 8):
        self.dataset_json = os.path.join(dir_main, "training_data_set", "dataset.json")
        self.data = []
        self.textList = []
        self.textList_cat = []
        self.random_state = state
        self._load_dataset()
        self._predict_model()
        self._model_accuracy()

    # Loads training set json file to train the model
    def _load_dataset(self):
        try:
            with open(self.dataset_json, "r") as file:
                self.data = json.load(file)
        except:
            print("dataset.json not found or empty dataset!")
            sys.exit()

        for item in self.data:
            self.textList += item["wordList"]
            self.textList_cat.append(item["Category"])

        # Splits data set into training/test. Default is 75%/25%
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.textList, self.textList_cat, test_size = 0.2, random_state=self.random_state)
        # print(len(self.textList))
        # print(len(self.X_train))
        # print(len(self.X_test))
        # print(len(self.y_train))
        # print(len(self.y_test))
        # print(self.y_test)

    # Fit training dataset into naive_bayes model
    def _predict_model(self):
        self.extractor = csV3.TextFeatureExtractor(self.X_train)
        df = self.extractor.df
        self.clf = MultinomialNB().fit(df, self.y_train)
        # df_consolidate = df
        # df_consolidate["Category"] = pd.Series(self.y_train)
        # df_group = df_consolidate.groupby('Category')
        # for x in df_group.groups:
        #     df_subset = df_group.get_group(x)
        #     print(df_subset["Category"].iloc[0])
        #     print((df_subset.T[df_subset.any()].T).shape)

    # Calculates the accurary of model based on training dataset
    def _model_accuracy(self):
        self.extractor_pred = csV3.TextFeatureExtractor(self.X_test, self.extractor.vectorizer, self.extractor.transformer, self.extractor.transformer_tfn, False)
        df = self.extractor_pred.df
        self.y_pred = self.clf.predict(df)
        self.accuracy = metrics.accuracy_score(self.y_test, self.y_pred)

    #Prints out confusion matrix of prediction based on training dataset
    def print_confu_matrix(self):
        print(pd.crosstab(pd.Series(self.y_test), pd.Series(self.y_pred), rownames=['True'], colnames=['Predicted'], margins=True))

    def print_class_report(self):
        print(metrics.classification_report(self.y_test, self.y_pred, digits = 4))



class PredictCat():

    # Class to predict categories based on tfidf input and word model
    def __init__(self, model, new_tfidf):
        self.tfidf = new_tfidf
        self.model = model
        self.predicted = []
        self.predict_prob = []
        self.confidence_threshold = 0.2
        self._predict_cat()
        self._top_cat()

    # Private function to predict given tfidf and calculate accuracy
    # Note: tfidf has to be extracted using self.extractor from this class
    # For each prediction, if confidence is < threshold, will be categorized as "None"
    def _predict_cat(self):
        self.predicted = self.model.clf.predict(self.tfidf)
        self.predict_prob = self.model.clf.predict_proba(self.tfidf)
        for i in range(len(self.predict_prob)):
            if max(self.predict_prob[i]) < self.confidence_threshold: self.predicted[i] = "None"

    # Calculates the number of websites for each category and sort them in order of frequency
    def _top_cat(self):
        count_list = []
        for item in self.predicted:
            if item != "None": count_list.append(item)
        self.cat_count = dict(Counter(count_list).most_common())
        self.cat_none_count = Counter(self.predicted)["None"]
        print(self.cat_count)
        print("None:", self.cat_none_count)




if __name__ == '__main__':
    word_relation = WordRelation()
    docs_new = ['I love to eat a lot of food. Bubble tea especially', 'Hiking up mountains are good for health', 'I love looking at the exhibits on historical figures', 'I like coffee', 'Nothing really interests me']
    X_new_counts = word_relation.extractor.vectorizer.transform(docs_new)
    X_new_tfidf = word_relation.extractor.transformer.transform(X_new_counts)

    predict_cat = PredictCat(word_relation, X_new_tfidf)
    predicted = predict_cat.predicted
    predicted_prob = predict_cat.predict_prob
    # print(predicted.size)

    for doc, category in zip(docs_new, predicted): print('%r => %s' % (doc, category))
    print(predicted_prob)

    print(word_relation.accuracy)
    word_relation.print_confu_matrix()
    word_relation.print_class_report()

    accuracy = []
    for i in range(50):
        word_relation = WordRelation(i)
        accuracy.append(word_relation.accuracy)
        print("%d : %f" % (i, word_relation.accuracy))
    print("Average accracy across 50 test/train sets:", round(sum(accuracy)/len(accuracy), 3))
