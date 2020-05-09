import os, json, shutil
from csv import writer, DictWriter, DictReader

DB_PATH = os.path.dirname(__file__)
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

class make_db:
    def __init__(self):
        self.db_path = DB_PATH

        self.attraction_path = os.path.normpath(
            os.path.join(self.db_path, r'Attraction_JSONs')
            )
        if os.path.exists(self.attraction_path) == False:
            raise Exception(
                'class make_csv: The sub-directory Attraction_JSONs is not found.')

        self.to_be_updated_path = os.path.normpath(
            os.path.join(self.attraction_path, r'to_be_updated')
        )
        if os.path.exists(self.to_be_updated_path) == False:
            raise Exception(
                'class make_csv: The sub-directory Attraction_JSONs/to_be_updated '
                'is not found'
            )

        self.updated_path = os.path.normpath(
            os.path.join(self.attraction_path, r'updated')
        )
        if os.path.exists(self.updated_path) == False:
            raise Exception(
                'class make_csv: The sub-directory Attraction_JSONs/updated '
                'is not found'
            )

        resource_path = os.path.normpath(
            os.path.join(self.db_path, r'resource')
        )
        if not os.path.exists(resource_path):
            os.makedirs(resource_path)
        self.resource_path = resource_path

        attraction_csv = os.path.normpath(
            os.path.join(self.resource_path, r'attraction.csv')
        )
        self.create_attraction_csv(attraction_csv)
        self.attraction_csv = attraction_csv

    def create_attraction_csv(self, csv_path):
        if os.path.exists(csv_path) == False:
            with open(csv_path, 'a+', newline='') as write_obj:
                header = ['country',
                          'city',
                          'exact_city',
                          'name',
                          'category',
                          'raw_ranking',
                          'ranking_position',
                          'rating',
                          'location_string',
                          'photo_url',
                          'web_url',
                          'address',
                          'phone',
                          'email',
                          'description'
                          ]
                csv_writer = writer(write_obj)
                csv_writer.writerow(header)

    def write_city_attraction_to_csv(self):
        for subdir, dirs, files in os.walk(self.to_be_updated_path):
            if subdir != self.to_be_updated_path:
                city = self.parse_for_city(subdir)
                for filename in os.listdir(subdir):
                    if filename == 'Attractions.json' or filename == 'Restaurants.json':
                        try:
                            print(f"Processing {filename} of {subdir}......")
                            json_file = os.path.normpath(
                                os.path.join(subdir, filename)
                            )
                            self.write_json_to_csv(json_file, city)
                        except Exception as e:
                            print(f"Writing to attraction.csv failed for "
                                  f"{json_file}")
                            print(str(e))
                    else:
                        continue
                shutil.move(subdir, self.updated_path)

    def write_json_to_csv(self, json_file, city):
        with open(json_file, 'r') as read_obj:
            json_data = json.load(read_obj)

        read_obj = DictReader(open(self.attraction_csv))
        fieldname = read_obj.fieldnames

        for entry in json_data:
            with open(self.attraction_csv, 'a+', newline="", encoding='utf-8') as write_obj:
                dict_writer = DictWriter(write_obj, fieldnames=fieldname)
                try:
                    entry_list = self.parse_entry_to_dict(entry)
                    for subentry in entry_list:
                        subentry['city'] = city
                    [dict_writer.writerow(subentry) for subentry in entry_list]
                except Exception as e:
                    print(f"{self.parse_entry_to_dict(entry)} omitted due to error.")
                    print(str(e))

    def parse_entry_to_dict(self, entry_dict):
        if 'name' not in entry_dict:
            return []

        if entry_dict['category']['key'] == 'restaurant':
            item_dict = {}
            try:
                item_dict['category'] = 'Food & Drink'
            except:
                item_dict['category'] = ''

            try:
                item_dict['name'] = entry_dict['name']
            except:
                item_dict['name'] = ''

            try:
                item_dict['raw_ranking'] = entry_dict['raw_ranking']
            except:
                item_dict['raw_ranking'] = ''

            try:
                item_dict['ranking_position'] = entry_dict['ranking_position']
            except:
                item_dict['ranking_position'] = ''

            try:
                item_dict['rating'] = entry_dict['rating']
            except:
                item_dict['rating'] = ''

            try:
                item_dict['location_string'] = entry_dict['location_string']
            except:
                item_dict['location_string'] = ''

            try:
                item_dict['photo_url'] = entry_dict['photo']['images']['original']['url']
            except:
                item_dict['photo_url'] = ''

            try:
                item_dict['web_url'] = entry_dict['web_url']
            except:
                item_dict['web_url'] = ''

            try:
                item_dict['address'] = entry_dict['address']
            except:
                item_dict['address'] = ''

            try:
                item_dict['country'] = entry_dict['address_obj']['country']
            except:
                item_dict['country'] = ''

            try:
                item_dict['exact_city'] = entry_dict['address_obj']['city']
            except:
                item_dict['exact_city'] = ''

            try:
                item_dict['phone'] = entry_dict['phone']
            except:
                item_dict['phone'] = ''

            try:
                item_dict['email'] = entry_dict['email']
            except:
                item_dict['email'] = ''

            try:
                item_dict['description'] = entry_dict['description']
            except:
                item_dict['description'] = ''

            return [item_dict]

        else:

            output = []
            for item in entry_dict['subcategory']:
                if not self.in_permitted_items(item['name']):
                    return []
                else:
                    item_dict = {}
                    try:
                        item_dict['category'] = item['name']
                    except:
                        item_dict['category'] = ''

                    try:
                        item_dict['name'] = entry_dict['name']
                    except:
                        item_dict['name'] = ''

                    try:
                        item_dict['raw_ranking'] = entry_dict['raw_ranking']
                    except:
                        item_dict['raw_ranking'] = ''

                    try:
                        item_dict['ranking_position'] = entry_dict['ranking_position']
                    except:
                        item_dict['ranking_position'] = ''

                    try:
                        item_dict['rating'] = entry_dict['rating']
                    except:
                        item_dict['rating'] = ''

                    try:
                        item_dict['location_string'] = entry_dict['location_string']
                    except:
                        item_dict['location_string'] = ''

                    try:
                        item_dict['photo_url'] = entry_dict['photo']['images']['original']['url']
                    except:
                        item_dict['photo_url'] = ''

                    try:
                        item_dict['web_url'] = entry_dict['web_url']
                    except:
                        item_dict['web_url'] = ''

                    try:
                        item_dict['address'] = entry_dict['address']
                    except:
                        item_dict['address'] = ''

                    try:
                        item_dict['country'] = entry_dict['address_obj']['country']
                    except:
                        item_dict['country'] = ''

                    try:
                        item_dict['exact_city'] = entry_dict['address_obj']['city']
                    except:
                        item_dict['exact_city'] = ''

                    try:
                        item_dict['phone'] = entry_dict['phone']
                    except:
                        item_dict['phone'] = ''

                    try:
                        item_dict['email'] = entry_dict['email']
                    except:
                        item_dict['email'] = ''

                    try:
                        item_dict['description'] = entry_dict['description']
                    except:
                        item_dict['description'] = ''

                output.append(item_dict)
                return output

    def in_permitted_items(self, item):
        if item in PERMITTED_ITEMS:
            return True
        else:
            return False

    def parse_for_city(self, dir):
        country, city = os.path.basename(dir).split('_')
        return city


db_make_obj = make_db()
db_make_obj.write_city_attraction_to_csv()















