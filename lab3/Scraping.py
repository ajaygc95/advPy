__author__ = "Ajay GC"

import pandas as pd
from database import Database


class Scrape:
    def __init__(self):
        self.url = 'https://www.esrl.noaa.gov/gmd/aggi/aggi.html'

    def parse(self):
        database = Database()
        database.createTable()
        dfs = pd.read_html(self.url, skiprows=range(2))
        final_table = dfs[1]
        for column, row in final_table.iterrows():
            database.insert(int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[5]),
                            float(row[6]))

# backend = Scrape()
# backend.parse()
