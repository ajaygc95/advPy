__author__ = "Ajay GC"

import  pandas as pd
import xml.etree.ElementTree as ET
from database import Database

class Scrape:
    def __init__(self):
        self.country_list = []

    def data_list(self):
        database = Database()

        # database.createTable()
        tree = ET.parse('UNData.xml')
        root = tree.getroot()
        for x in root.findall('data'):
            for item in x.findall('record'):
                country = item.find('Country').text
                year = item.find('Year').text
                value = item.find('Value').text

                database.insert(country,year,value)
                if country not in self.country_list:
                    self.country_list.append(country)
        return self.country_list

# scrape = Scrape()
# scrape.data_list()



