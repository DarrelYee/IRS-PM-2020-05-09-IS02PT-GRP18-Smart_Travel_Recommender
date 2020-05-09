from city_selector import city_selector
from random import randint

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

total_test = 30
for iter in range(total_test):
    print(f"======================================= Run {iter + 1}===========================================")
    ranked_preference = {}
    unranked_preference = []

    rand1 = randint(0,7)
    ranked_preference[PERMITTED_ITEMS[rand1]] = '1'
    unranked_preference.append(PERMITTED_ITEMS[rand1])

    rand2 = randint(0, 7)
    while rand2 == rand1:
        rand2 = randint(0,7)
    ranked_preference[PERMITTED_ITEMS[rand2]] = '2'
    unranked_preference.append(PERMITTED_ITEMS[rand2])

    rand3 = randint(0, 7)
    while (rand3 == rand2) or (rand3 == rand1):
        rand3 = randint(0,7)
    ranked_preference[PERMITTED_ITEMS[rand3]] = '3'
    unranked_preference.append(PERMITTED_ITEMS[rand3])

    ranked_selector = city_selector()
    unranked_selector = city_selector()
    print(f"Ranked preference is: {ranked_preference}")
    print(f"Unranked preference is: {unranked_preference}")

    ranked_matching = ranked_selector.find_matching_city(ranked_preference)

    print("Matching city based on ranked preference: ")
    print(ranked_matching['matching_city'])
    print("\n")
    unranked_matching = unranked_selector.find_matching_city(unranked_preference)

    print("Matching result based on unranked preference: ")
    print(unranked_matching['matching_city'])
    print("\n")