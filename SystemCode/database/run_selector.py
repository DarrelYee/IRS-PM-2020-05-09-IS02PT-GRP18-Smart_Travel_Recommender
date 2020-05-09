from city_selector import city_selector

RANKED_USER_PREFERENCE_1 = {
    'Museums' : '2',
    'Spas & Wellness' : '1',
    'Outdoor Activities' : '3'
}

RANKED_USER_PREFERENCE_2 = {
    'Food & Drink' : '2',
    'Nightlife' : '1',
    'Sights & Landmarks' : '3'
}

RANKED_USER_PREFERENCE_3 = {
    'Nature & Parks' : '1',
    'Sights & Landmarks' : '2',
    'Outdoor Activities' : '3'
}

USER_PREFERENCE = [
    'Shopping',
    'Nightlife',
    'Spas & Wellness'
]

#*******************************************************************
# Use city_selector.
#*******************************************************************

# Comment out one of the two lines below to either select a ranked or unranked preference
#SELECTED_PREFERENCE = RANKED_USER_PREFERENCE
SELECTED_PREFERENCE = RANKED_USER_PREFERENCE_1

# Initiate a city_selector object
selector_obj = city_selector()

# Select matching city along with at most 5 activities of each user's preferred activity
# in the form of dictionary:
# {'matching_city': '<Matching_city>, '<category1>' : [List of activities]
#                                   , '<category2>': [List of activities]
#                                   , '<category3>' : [List of activities]
#                                   , 'choice_ranking' : <rank of choice>}
# Each element in the list of activities is a dictionary containing the following keys:
# 1. country
# 2. city
# 3. exact_city
# 4. name
# 5. category
# 6. raw_ranking
# 7. ranking_position
# 8. rating
# 9. location_string
# 10. photo_url
# 11. web_ur;
# 12. address
# 13. phone
# 14. email
# 15. description
matching_city_and_activity, list_of_matching_city_and_activity = selector_obj.find_matching_city(RANKED_USER_PREFERENCE_2)
print(matching_city_and_activity)
print("\n")
print("========= list of matching city ==========")
for item in list_of_matching_city_and_activity:
    print(f"Matching city at choice: {item['choice_ranking']} is {item['matching_city']}")

# View the selection_score and selection_rank of each city based on user's preference
# in the form of Pandas Dataframe:
# ==================================================================================
#   city  ||  magnitude_score ||  order_score ||  selection_score ||  rank    ||
# ==================================================================================
#  Aomori ||    0.378235      ||    0.122829  ||   0.259532       ||  20.0    ||
# ==================================================================================
# .........
#  Tokyo  ||    0.392976      ||    0.161135  ||   0.277055       ||  8.0     ||
# ==================================================================================
selection_score_rank = selector_obj.compute_selection_score(RANKED_USER_PREFERENCE_2)
selection_score_rank = selection_score_rank.sort_values(
    by=['selection_rank'],
    ascending=True
)
print("\n")
print("========== Selection score and ranking ==========")
print(selection_score_rank)

# ==================================================================================


