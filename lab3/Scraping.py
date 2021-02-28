__author__ = "Ajay GC"
import pandas as pd
from database import Database


class Backend:
    def __init__(self):
        self.url = 'https://www.esrl.noaa.gov/gmd/aggi/aggi.html'

    def parse(self):
        database = Database()
        database.createTable()
        dfs = pd.read_html(self.url, skiprows=range(3))
        final_table = dfs[1]

        for column, row in final_table.iterrows():
            database.insert(int(row['Year']), float(row['CO2']), float(row['CH4']),float(row['N2O']) , float(row['CFC12']), float(row['CFC11']), float(row['15-minor']))
            # print(row)


backend = Backend()
backend.parse()
