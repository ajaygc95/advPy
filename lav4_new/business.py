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
            json.dump(dict1,jsonfile)

        json_data = json.dumps(dict1)

        print(type(json_data))
        type_data = json.loads(json_data)
        print(type(type_data))
        return json_data

# business = Business()
# business.countryData('Australia')