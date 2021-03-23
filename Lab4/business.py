__author__ = "Ajay GC"

from database import Database
import json


class Business:

    def countryData(self, country_name):
        dict1 = {}
        database = Database()
        country_data = database.get_value(country_name)

        for item in country_data:
            dict1[item[1]] = item[2]

        with open('json_data.json', 'w') as jsonfile:
            json.dump(sorted(dict1.items(), key=lambda x: x[0]), jsonfile)

        json_data = json.dumps(sorted(dict1.items(), key=lambda x: x[0]), jsonfile)

        return json_data
