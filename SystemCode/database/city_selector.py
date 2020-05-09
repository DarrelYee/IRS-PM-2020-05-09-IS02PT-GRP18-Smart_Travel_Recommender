import numpy as np
import pandas as pd

import os, sys
dir_main = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_CSV = os.path.join(dir_main, "database", "resource", "attraction.csv")
#DB_CSV = r"resource\attraction.csv"

RANKING_THRESHOLD = 3.5
INTRA_WEIGHT = 0.5
ORDER_WEIGHT = 0.5

PERMITTED_ITEMS = [
    'Museums',
    'Outdoor Activities',
    'Nature & Parks',
    'Shopping',
    'Spas & Wellness',
    'Food & Drink',
    'Nightlife',
    'Sights & Landmarks'
]
RANKLESS_ITEMS = [
    'Nightlife',
    'Spas & Wellness',
    'Outdoor Activities'
]
pd.set_option("display.max_columns", None)
class city_selector:

    def __init__(self, db_csv = DB_CSV):
        self.database_df = pd.read_csv(db_csv, skipinitialspace=True)
        self.total_df = self.count_category_items(self.database_df)
        self.top_df = self.count_top_items(self.database_df)
        self.category_min_max_df = self.min_max_of_each_category(self.database_df)
        self.city_score_rank_df = self.city_category_score(self.database_df)
        self.min_overall_result = 5
        self.min_result_per_category = 3

    def count_category_items(self, database_df):
        total_df = database_df.groupby(['city', 'category'], as_index=False)['country'].count()
        total_df.rename({'country' : 'count'}, axis='columns', inplace=True)
        return total_df

    def min_max_of_each_category(self, database_df):
        total_df = self.count_category_items(database_df)
        sum_of_each_category_df = total_df.groupby(['category'], as_index=False).agg({'count':['min', 'max', 'sum']})
        return sum_of_each_category_df

    def count_top_items(self, database_df):
        database_df['above_threshold'] =  database_df['raw_ranking'].apply(self.is_above_threshold)
        top_df = database_df[database_df['above_threshold']==True]
        top_df = top_df.groupby(['city', 'category'], as_index=False)['above_threshold'].count()
        top_df.rename({'above_threshold' : 'count'}, axis='columns', inplace=True)
        return top_df

    def city_category_score(self, database_df):
        total_df = self.count_category_items(database_df)
        top_df = self.count_top_items(database_df)
        category_min_max_df = self.min_max_of_each_category(database_df)
        score_df = pd.DataFrame(columns=['city',
                                         'category',
                                         'intra_score',
                                         'inter_score',
                                         'category_score'])

        for city in total_df['city'].unique():
            for category in PERMITTED_ITEMS:
                row_dict = {}
                row_dict['city'] = city
                row_dict['category'] = category

                #Calculate intra_score
                try:
                    top_count = float(top_df[(top_df['city']==city) &
                                             (top_df['category']==category)]
                                      ['count'])
                    #print(f'city: {city}, category: {category}, {top_count}')
                except:
                    #print(f'city: {city}, category: {category}, top error')
                    top_count = 0

                try:
                    total_count = float(total_df[(total_df['city']==city) &
                                                 (total_df['category']==category)]
                                        ['count'])
                    #print(f'city: {city}, category: {category}, {total_count}')
                except:
                    total_count = 0
                    #print(f'city: {city}, category: {category}, total error')

                try:
                    row_dict['intra_score'] = top_count / total_count
                except:
                    row_dict['intra_score'] = 0

                '''
                if total_count <= 3:
                    row_dict['intra_score'] = 0
                '''

                #Calculate inter_score
                '''
                category_min = \
                    float(category_min_max_df[category_min_max_df['category']==category]
                          ['count']['min'])
                '''
                category_min = 0
                category_max = \
                    float(category_min_max_df[category_min_max_df['category']==category]
                          ['count']['max'])
                row_dict['inter_score'] = (total_count - category_min) / \
                                          (category_max - category_min)
                '''
                if category in RANKLESS_ITEMS:
                    intra_weight = 0
                else:
                    intra_weight = INTRA_WEIGHT
                '''
                intra_weight = INTRA_WEIGHT
                row_dict['category_score'] = \
                    intra_weight * row_dict['intra_score'] + \
                    (1 - intra_weight) * row_dict['inter_score']

                #row_dict['category_score'] = row_dict['intra_score'] * row_dict['inter_score']

                score_df = score_df.append(row_dict, ignore_index=True)

        score_df['category_rank'] = score_df.groupby(['city'])['category_score'].\
            rank(ascending=False)
        return score_df

    def is_above_threshold(self, x):
        return x >= RANKING_THRESHOLD

    def compute_selection_score(self, user_preference):
        if isinstance(user_preference, dict):
            selection_dict = {'city': [],
                              'magnitude_score': [],
                              'order_score': [],
                              'selection_score': []}

            magnitude_score = 0
            order_score = 0
            for city in self.city_score_rank_df['city'].unique():
                selection_dict['city'].append(city)

                selection_score = 0
                for category in list(user_preference.keys()):
                    #print(f"Processing category: {category} of city: {city}......")
                    city_category_score = self.city_score_rank_df[
                        (self.city_score_rank_df['city']==city) &
                        (self.city_score_rank_df['category']==category)
                    ]['category_score']
                    city_category_rank = self.city_score_rank_df[
                        (self.city_score_rank_df['city']==city) &
                        (self.city_score_rank_df['category']==category)
                    ]['category_rank']
                    user_rank = user_preference[category]
                    magnitude_score += (1 - float(city_category_score))**2
                    order_score += (float(user_rank) - float(city_category_rank))**2

                magnitude_score = 1 / (1 + np.sqrt(magnitude_score))
                selection_dict['magnitude_score'].append(magnitude_score)

                order_score = 1 / (1 + np.sqrt(order_score))
                selection_dict['order_score'].append(order_score)

                order_weight = ORDER_WEIGHT
                selection_score = \
                    (1 - order_weight ) * magnitude_score + order_weight * order_score
                selection_dict['selection_score'].append(selection_score)

            selection_score_df = pd.DataFrame(selection_dict,
                                              columns=['city',
                                                       'magnitude_score',
                                                       'order_score',
                                                       'selection_score'])
            selection_score_df['selection_rank'] = selection_score_df['selection_score'].\
                rank(ascending=False)

            return selection_score_df

        elif isinstance(user_preference, list):
            selection_dict = {'city': [],
                              'selection_score':[]}

            for city in self.city_score_rank_df['city'].unique():
                #print(f"Processing category: {category} of city: {city}......")
                selection_dict['city'].append(city)

                selection_score = 0
                for category in user_preference:
                    category_score = self.city_score_rank_df[
                        (self.city_score_rank_df['city']==city) &
                        (self.city_score_rank_df['category']==category)
                    ]['category_score']
                    selection_score += (1 - float(category_score))**2
                selection_score = 1 / (1 + np.sqrt(selection_score))

                selection_dict['selection_score'].append(selection_score)

            selection_score_df = pd.DataFrame(selection_dict,
                                              columns=['city',
                                                       'selection_score'])
            selection_score_df['selection_rank'] = selection_score_df['selection_score'].\
                rank(ascending=False)

            return selection_score_df

    def find_matching_city(self, user_preference, no_of_activity=5):
        selection_score_df = self.compute_selection_score(user_preference)
        selection_score_df = selection_score_df.sort_values(
            by=['selection_rank']
        )

        first_flag = 1
        output_list = []
        choice_rank = 1
        for index in range(len(selection_score_df)):
            # Intialize variables
            total_activity = 0
            min_activity_per_category = 10000
            output_dict = {}
            top_rank = selection_score_df.iloc[index]['selection_rank']
            matching_city = selection_score_df.iloc[index]['city']
            #print(f"Current city is: {matching_city} at rank {top_rank}")

            # Set the current city as the matching city
            output_dict['matching_city'] = matching_city
            if index == 0:
                backup_dict = {}
                backup_dict['matching_city'] = matching_city

            # Convert preference in dictionary to list
            if isinstance(user_preference, dict):
                user_preference = list(user_preference.keys())

            for category in user_preference:
                # Detect if the category has any entry in the database
                #print(f"Processing category {category}")
                try:
                    # Find the total number of activity for the current category
                    no_of_total_activity = self.total_df[
                        (self.total_df['city'] == matching_city) &
                        (self.total_df['category'] == category)
                        ]['count'].values[0]
                    #print('try')
                except:
                    output_dict[category] = []
                    #print(f"Category {category} has no entry for the current city.")
                    min_activity_per_category = 0
                    #print('except')

                    # backup the entry of the first city
                    if index == 0:
                        backup_dict[category] = []
                    continue

                city_activity_df = self.database_df[
                    (self.database_df['city'] == matching_city) &
                    (self.database_df['category'] == category)
                    ]

                no_of_selected_activity = min(no_of_activity,
                                              no_of_total_activity)
                total_activity += no_of_selected_activity
                min_activity_per_category = min(no_of_selected_activity,
                                                min_activity_per_category)

                try:
                    city_activity_df = city_activity_df.sort_values(
                        by=['raw_ranking'],
                        ascending=False
                    ).head(no_of_selected_activity)
                    output_dict[category] = city_activity_df.to_dict('records')

                    # backup the entry of the first city
                    if index == 0:
                        backup_dict[category] = city_activity_df.to_dict('records')

                except:
                    city_activity_df = city_activity_df.head(no_of_selected_activity)
                    output_dict[category] = city_activity_df.to_dict('records')

                    # backup the entry of the first city
                    if index == 0:
                        backup_dict[category] = city_activity_df.to_dict('records')

            if ((total_activity >= self.min_overall_result) and
                    (min_activity_per_category >= self.min_result_per_category)):
                #print(f"total activity is {total_activity}")
                #print(f"minimum activity is {min_activity_per_category}")
                if first_flag == 1:
                    output_dict['choice_ranking'] = choice_rank
                    choice_rank += 1
                    first_output = output_dict
                    output_list.append(output_dict)
                    first_flag = 0
                else:
                    output_dict['choice_ranking'] = choice_rank
                    choice_rank += 1
                    output_list.append(output_dict)
            else:
                continue

        if output_list==[]:
            backup_dict['choice_rank'] = 1
            first_output = backup_dict
            output_list.append(first_output)

        return first_output, output_list






