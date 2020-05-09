from tkinter import *
from urllib import request
from pyke import knowledge_engine, krb_traceback
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from threading import Thread
from time import sleep, perf_counter
from queue import Queue
    
from View import *
from Activity import *
from Question import *
from questions_list import *
import copy
import numpy as np

import os, sys
dir_main = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(dir_main, "Smart_Travel_Recommender"))
sys.path.append(os.path.join(dir_main, "google_custom_search"))
sys.path.append(os.path.join(dir_main, "word_relation"))
sys.path.append(os.path.join(dir_main, "training_data_set"))
sys.path.append(os.path.join(dir_main, "database"))

import custom_search_V3 as Search
import word_relation_V2 as Preferences
import city_selector as Selector


class Controller:

    MIN_HISTORY = 35
    MAX_HISTORY = 1000
    MIN_SEARCHES = 2
    MIN_PREFERENCES = 2
    MAX_ACTIVITY_PER_PAGE = 4
    SEARCH_TIME_PER_TERM = 2.5


    UI_TITLE = "A Smart Travel Recommender"
    ICON_LINK = r'images\travel.ico'
    LOAD_LINK = r'images\please_wait.jpg'
    START_LINK = r'images\wunderlust.png'

    ACKNOWLEDGEMENT_LOAD = "Loading image from https://www.flickr.com/photos/janpersiel/27706588173"
    ACKNOWLEDGEMENT_ICON = "Icon made by Freepik from www.flaticon.com"
    ACKNOWLEDGEMENT_START = "Start image from https://www.uihere.com/"

    WELCOME_MESSAGE = "Welcome to our Smart Travel Recommender!"
    ONLINE_LOADING_MESSAGE = "Please wait while the app makes a prediction based on your internet history. Please use the skip button to stop the search at anytime. Stopping the search prematurely might affect prediction accuracy. The app does not store any data from the user."

    OFFLINE_QUESTION_INSTRUCTIONS = "Please answer the demographic and preference questions in the next 2 tabs using the sidebar. This will help us predict the places and activities that you will prefer to travel to."
    OFFLINE_MODE_MESSAGE = "This app is currently operating in offline mode."
    OFFLINE_MODE_ASSISTANCE_MESSAGE = "To enable more personalised predictions based on your search history, please restart the app after ensuring that you are connected to the internet and have sufficient search history stored."

    ACTIVIY_INSTRUCTIONS = "The app has sucessfully suggested a travel location and activites to do based on your internet search history. Please see the location and suggested activites using the sidebar."
    ONLINE_MODE_MESSAGE = "This app is currently operating in online mode."
    ONLINE_MODE_ASSISTANCE_MESSAGE = "The app uses your Chrome search history data stored on your computer to make a prediction. The app does not store any data from the user. To run the app wihout using your search history, run the app in offline mode. Please restart the app after you have switched off your internet."

    RBS_CATEGORIES_DICT = { "sights" : "Sights & Landmarks",
                            "dining" : "Food & Drink",
                            "shopping" : "Shopping",
                            "outdoor" : "Outdoor Activities",
                            "cultural" : "Museums",
                            "relaxation" : "Spas & Wellness",
                            "nightlife" : "Nightlife",
                            "nature" : "Nature & Parks"}


    SEARCH_CATEGORIES_DICT = {  "Sight and Landmarks": "Sights & Landmarks",
                                "Food and Drinks" : "Food & Drink",
                                "Shopping" : "Shopping",
                                "Outdoor Activities" : "Outdoor Activities",
                                "Museums" : "Museums",
                                "Relaxation" : "Spas & Wellness",
                                "Nightlife" : "Nightlife",
                                "Nature" : "Nature & Parks"}

    SURVEY_RANKINGS_POINTS = {  "Nature & Parks" : 0.8,
                                "Sights & Landmarks": 0.7,
                                "Food & Drink" : 0.6,
                                "Spas & Wellness" : 0.5,
                                "Outdoor Activities" : 0.4,
                                "Museums" : 0.3,
                                "Shopping" : 0.2,
                                "Nightlife" : 0.1}

    LOADING_PAGES_DICT = {"load": "Loading"}


    OFFLINE_PAGES_DICT_Q = {"start":"Start",
                            "question1":"About You? - 1",
                            "question2":"About You? - 2"}

    ACTIVITY_PAGES_DICT_2 = {"start":"Start",
                            "top1":"Our Pick! - 1",
                            "top2":"Our Pick! - 2"}

    ACTIVITY_PAGES_DICT_3 = {"start":"Start",
                            "top1":"Our Pick! - 1",
                            "top2":"Our Pick! - 2",
                            "top3":"Our Pick! - 3"}


    INDEX_ANSWER_DICT = {   0 : 'a',
                            1 : 'b',
                            2 : 'c',
                            3 : 'd'}

    instance = None


    def __init__(self):

        if Controller.instance != None:
            raise Exception("Controller is a Singleton Class")
        else:
            Controller.instance = self

        self.root = Tk()
        self.view = View(self.root)
        self.view.bind_to(self.update_screen, self.present_activities, self.redo, self.next)
        self.is_running = True
        self.mode = None


    def update_screen(self, view_type):
        self.view.raise_frame(view_type)


    def redo(self):
        self.mode = "offline"
        self.run_offline_questionaire()


    def next(self):
        if self.mode == "online":
            self.show_online_result()

        elif self.mode == "offline":
            self.show_offline_result()


    def run_offline_questionaire(self):

        self.set_window(800, 1000)
        self.view.set_frames(frame_names = self.OFFLINE_PAGES_DICT_Q.keys())
        self.view.menu_template()

        self.view.header_template("start", self.WELCOME_MESSAGE)
        self.view.header_template("question1", "Tell us more about yourself!")
        self.view.header_template("question2", "Tell us more about yourself!")


        self.view.sidebar_template(self.OFFLINE_PAGES_DICT_Q)
        self.view.footer_template(self.ACKNOWLEDGEMENT_START + " .-.-. " + self.ACKNOWLEDGEMENT_ICON)

        self.view.start_template(   "start",
                                    instructions = self.OFFLINE_QUESTION_INSTRUCTIONS,
                                    mode = self.OFFLINE_MODE_MESSAGE,
                                    mode_assistance = self.OFFLINE_MODE_ASSISTANCE_MESSAGE,
                                    image_link = self.START_LINK)
        self.view.question_template("question1", question_list1, False)
        self.view.question_template("question2", question_list2, True)

        self.update_screen("start")


    def present_activities(self):

        if self.mode == "online":
            self.is_running = False

        elif self.mode == "offline":
            self.answer_list = []

            for items in question_list1:
                for i in range(len(items.answer)):
                    if items.answer[i] == True:
                        self.answer_list.append((items.question_num, self.INDEX_ANSWER_DICT[i]))

            for items in question_list2:
                for i in range(len(items.answer)):
                    if items.answer[i] == True:
                        self.answer_list.append((items.question_num, self.INDEX_ANSWER_DICT[i]))

            engine = knowledge_engine.engine(__file__)
            engine.reset()
            engine.activate('category_rules')

            for answers in self.answer_list:
                engine.assert_('answer', 'question', answers)

            print("Facts gathered:")
            engine.get_kb('answer').dump_specific_facts()

            try:
                vars, plan =  engine.prove_1_goal('category_rules.top2($category1, $category2)')
                print()
                print("Top 2 Activity Categories selected are: %s, %s" % (self.RBS_CATEGORIES_DICT[vars['category1']], self.RBS_CATEGORIES_DICT[vars['category2']]))
                print()
            except knowledge_engine.CanNotProve:
                krb_traceback.print_exc()

            self.user_preferences = list((self.RBS_CATEGORIES_DICT[vars['category1']], self.RBS_CATEGORIES_DICT[vars['category2']]))
            selector_obj = Selector.city_selector()
            throwaway, self.cities_and_activities_results_list = selector_obj.find_matching_city(self.user_preferences)
            self.show_offline_result()
            

    def show_offline_result(self):
        current_city_and_activities = self.cities_and_activities_results_list[0]
        self.have_next_city = False

        if len(self.cities_and_activities_results_list) > 1:
            self.cities_and_activities_results_list = self.cities_and_activities_results_list[1:]
            self.have_next_city = True

        self.city = current_city_and_activities.pop("matching_city")
        print(current_city_and_activities.pop("choice_ranking"))
        self.matching_activity = current_city_and_activities
        self.country = self.matching_activity[self.user_preferences[0]][0]["country"]

        self.ACTIVITY_PAGES_DICT_2["top1"] = self.user_preferences[0]
        self.ACTIVITY_PAGES_DICT_2["top2"] = self.user_preferences[1]

        self.set_window(800, 1000)
        self.view.set_frames(frame_names = self.ACTIVITY_PAGES_DICT_2.keys())
        self.view.menu_template()

        self.view.header_template("start", self.WELCOME_MESSAGE)

        self.view.sidebar_template(self.ACTIVITY_PAGES_DICT_2)
        self.view.footer_template(self.ACKNOWLEDGEMENT_START + " .-.-. " + self.ACKNOWLEDGEMENT_ICON)

        self.view.start_template(   "start",
                                    remarks = self.ACTIVIY_INSTRUCTIONS,
                                    mode = self.OFFLINE_MODE_MESSAGE,
                                    mode_assistance = self.OFFLINE_MODE_ASSISTANCE_MESSAGE,
                                    image_link = self.START_LINK,
                                    redo_mode = self.mode,
                                    have_next_city = self.have_next_city,
                                    instructions = "Top 2 activity categories selected are: %s & %s. The app has predicted that your next travel location will be: %s, %s." \
                                        % (self.user_preferences[0], self.user_preferences[1], self.country, self.city))

        activities = self.create_activities(0)
        self.view.header_template("top1", "Our picks for you in " + self.city + " for " + self.user_preferences[0])
        self.view.activity_template("top1", activities)

        activities = self.create_activities(1)
        self.view.header_template("top2", "Our picks for you in " + self.city + " for " + self.user_preferences[1])
        self.view.activity_template("top2", activities)

        self.update_screen("start")


    def create_activities(self, index):
        activities = []
        activity_count = 0
        for activity in self.matching_activity[self.user_preferences[index]]:
            if activity_count < self.MAX_ACTIVITY_PER_PAGE:
                activity_count += 1
                print(activity)
                print()
                activities.append(
                    Activity(   category=self.user_preferences[index],
                                country=self.city,
                                location=activity["location_string"],
                                activity_name=activity["name"],
                                address=activity["address"],
                                description=activity["description"],
                                web_url=activity["web_url"],
                                image_link=activity["photo_url"]))

        return activities


    '''
    Function: Setting general window parameters (Title, Icon, Size)
    '''
    def set_window(self, width, height):
        self.view.set_title(self.UI_TITLE)
        self.view.set_icon(self.ICON_LINK)
        self.view.set_window_size(width, height)

    def has_internet(self, host='http://google.com'):
        try:
            request.urlopen(host)
            print("Connected to the internet")
            return True
        except:
            print("Not connected to the internet")
            print()
            return False

    def has_internet_history(self, sample_file):
        try:
            if sample_file is not None:
                sampleChromeHistoryDir = os.path.join(dir_main, "samples")
                self.hist = Search.History(sensitivity = 1, chromeHistoryDir = sampleChromeHistoryDir, sampleFile = sample_file)
            else:
                self.hist = Search.History(sensitivity = 1)
        except:
            self.root.withdraw()
            print("There was an error collecting your browser history. PLease ensure that your Chrome broswer is closed before trying again.")
            self.view.popup("Error", "There was an error collecting your browser history. PLease ensure that your Chrome broswer is closed before trying again.")
            sys.exit(1)

        if len(self.hist.searches) >= self.MAX_HISTORY:
            self.hist.searches = self.hist.searches [(len(self.hist.searches)-self.MAX_HISTORY):]

        print(len(self.hist.searches), 'search terms returned')
        if len(self.hist.searches) >= self.MIN_HISTORY:
            print("Has sufficent internet history. More than", self.MIN_HISTORY, "search entries")
            print()
            return True
        else:
            print("Has insufficent internet history. Less than", self.MIN_HISTORY, "search entries")
            print()
            return False

    def run(self, sample_file = None):
        if self.has_internet() and self.has_internet_history(sample_file):
            try:
                self.mode = "online"
                self.run_loading_screen()
                t1 = Thread(target=self.run_search_categorisation)
                t1.start()

            except:
                print("Error found when searching using online mode. Switching to offline mode.")
                self.view.popup("Error", "Error found when searching using online mode. Switching to offline mode.")
                self.mode = "offline"
                self.run_offline_questionaire()
        else:
            self.mode = "offline"
            self.run_offline_questionaire()

        self.root.mainloop()


    def run_loading_screen(self):

        self.set_window(500, 420)
        self.view.set_frames(frame_names = self.LOADING_PAGES_DICT.keys())

        addtional_message = f"You currently have {len(self.hist.searches)} entries. It will take approximately {int(np.ceil(len(self.hist.searches)*self.SEARCH_TIME_PER_TERM/60))} mins to finish the search"

        self.view.header_template("load", "Loading")
        self.view.footer_template(self.ACKNOWLEDGEMENT_LOAD)
        self.view.load_template("load",
                                self.ONLINE_LOADING_MESSAGE,
                                addtional_message,
                                self.LOAD_LINK)


    def run_search_categorisation(self):

        start_time = perf_counter()
        searchEngine = Search.TermSearch()
        searchCount = 0
        urlList = []
        textList = []

        for query in self.hist.searches:
            # Search for URLs
            if self.is_running:
                try:
                    url = searchEngine.getSearchResultV3(query)
                    searchCount += 1
                    print("Search", searchCount, "completed for terms", query)
                except Exception as e:
                    print(e)
                    print("Error searching for websites with search terms, skipping...")
                    continue

            # Search for site texts
                try:
                    siteText = searchEngine.getSiteText(url)
                    textList += [siteText]
                    urlList.append(url)
                    print("Text collected for", searchCount)
                except Exception as e:
                    print(e)
                    print("Error visiting URL, skipping...")

        self.user_preferences = []

        if len(textList) >=  self.MIN_SEARCHES:
            word_relation = Preferences.WordRelation()

            extractor = Search.TextFeatureExtractor(textList, word_relation.extractor.vectorizer, word_relation.extractor.transformer, word_relation.extractor.transformer_tfn, parent = False)
            browser_predict = Preferences.PredictCat(word_relation, extractor.df)

            predicted = browser_predict.predicted
            predicted_prob = browser_predict.predict_prob
            for url, prediction, predict_prob in zip(urlList, predicted, predicted_prob): print('%r => %s %s' % (url, prediction, predict_prob))

            end_time = perf_counter()
            print("Time taken for search is:", end_time-start_time)
            print()

            self.category_counts = browser_predict.cat_count
            cat_count = copy.copy(browser_predict.cat_count)

            for category, count in cat_count.items():
                count += self.SURVEY_RANKINGS_POINTS[self.SEARCH_CATEGORIES_DICT[category]]
                cat_count[category] = count

            rank = 0
            max_count = 0
            cat_ranked = {}
            for _ in range(len(cat_count)):
                for category, count in cat_count.items():
                    if count > max_count:
                        max_count = count
                        highest_rank = category

                rank += 1
                cat_count[highest_rank] = -1
                cat_ranked[self.SEARCH_CATEGORIES_DICT[highest_rank]] = rank
                self.user_preferences.append(self.SEARCH_CATEGORIES_DICT[highest_rank])
                previous_count = max_count
                max_count = 0

        if len(self.user_preferences) < self.MIN_PREFERENCES:
            print("Unable to determine user preferences, switching back to offline app")
            self.view.popup("Infomation", "Unable to determine user preferences, switching back to offline app")
            self.mode = "offline"
            self.run_offline_questionaire()

        else:
            print("Top Activity Categories selected are:", cat_ranked)
            print()

            selector_obj = Selector.city_selector()
            throwaway, self.cities_and_activities_results_list = selector_obj.find_matching_city(cat_ranked)
            self.show_online_result()


    def show_online_result(self):

        self.set_window(800, 1000)

        current_city_and_activities = self.cities_and_activities_results_list[0]
        self.have_next_city = False

        if len(self.cities_and_activities_results_list) > 1:
            self.cities_and_activities_results_list = self.cities_and_activities_results_list[1:]
            self.have_next_city = True

        self.city = current_city_and_activities.pop("matching_city")
        print(current_city_and_activities.pop("choice_ranking"))
        self.matching_activity = current_city_and_activities
        self.country = self.matching_activity[self.user_preferences[0]][0]["country"]


        if len(self.user_preferences) == 2:
            self.view.set_frames(frame_names = self.ACTIVITY_PAGES_DICT_2.keys())
            self.ACTIVITY_PAGES_DICT_2["top1"] = self.user_preferences[0]
            self.ACTIVITY_PAGES_DICT_2["top2"] = self.user_preferences[1]
            self.view.sidebar_template(self.ACTIVITY_PAGES_DICT_2)

            activities = self.create_activities(0)
            self.view.header_template("top1", "Our picks for you in " + self.city + " for " + self.user_preferences[0])
            self.view.activity_template("top1", activities)

            activities = self.create_activities(1)
            self.view.header_template("top2", "Our picks for you in " + self.city + " for " + self.user_preferences[1])
            self.view.activity_template("top2", activities)

            self.view.start_template(   "start",
                                        remarks = self.ACTIVIY_INSTRUCTIONS,
                                        mode = self.ONLINE_MODE_MESSAGE,
                                        mode_assistance = self.ONLINE_MODE_ASSISTANCE_MESSAGE,
                                        image_link = self.START_LINK,
                                        redo_mode = self.mode,
                                        have_next_city = self.have_next_city,
                                        count_graph = self.category_counts,
                                        instructions = "Top 2 activity categories selected are: %s and %s. The app has predicted that your next travel location will be: %s, %s." \
                                            % (self.user_preferences[0], self.user_preferences[1], self.country, self.city))

        if len(self.user_preferences) >= 3:
            self.view.set_frames(frame_names = self.ACTIVITY_PAGES_DICT_3.keys())
            self.ACTIVITY_PAGES_DICT_3["top1"] = self.user_preferences[0]
            self.ACTIVITY_PAGES_DICT_3["top2"] = self.user_preferences[1]
            self.ACTIVITY_PAGES_DICT_3["top3"] = self.user_preferences[2]
            self.view.sidebar_template(self.ACTIVITY_PAGES_DICT_3)

            activities = self.create_activities(0)
            self.view.header_template("top1", "Our picks for you in " + self.city + " for " + self.user_preferences[0])
            self.view.activity_template("top1", activities)

            activities = self.create_activities(1)
            self.view.header_template("top2", "Our picks for you in " + self.city + " for " + self.user_preferences[1])
            self.view.activity_template("top2", activities)

            activities = self.create_activities(2)
            self.view.header_template("top3", "Our picks for you in " + self.city + " for " + self.user_preferences[2])
            self.view.activity_template("top3", activities)

            self.view.start_template(   "start",
                                        remarks = self.ACTIVIY_INSTRUCTIONS,
                                        mode = self.ONLINE_MODE_MESSAGE,
                                        mode_assistance = self.ONLINE_MODE_ASSISTANCE_MESSAGE,
                                        image_link = self.START_LINK,
                                        redo_mode = self.mode,
                                        have_next_city = self.have_next_city,
                                        count_graph = self.category_counts,
                                        instructions = "Top 3 activity categories selected are: %s, %s and %s. The app has predicted that your next travel location will be: %s, %s." \
                                            % (self.user_preferences[0], self.user_preferences[1], self.user_preferences[2], self.country, self.city))

        self.view.menu_template()
        self.view.header_template("start", self.WELCOME_MESSAGE)
        self.view.footer_template(self.ACKNOWLEDGEMENT_START + " .-.-. " + self.ACKNOWLEDGEMENT_ICON)

        self.update_screen("start")


if __name__ == '__main__':
    # Set working directory to always be current script folder
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    os.chdir(ROOT_PATH)

    if len(sys.argv) == 2:
        travel_app = Controller()
        travel_app.run(sys.argv[1])
    else:
        travel_app = Controller()
        travel_app.run()
