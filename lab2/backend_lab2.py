__author__ = "Ajay GC"

from bs4 import  BeautifulSoup
import requests
import pandas as pd
import re

from DataBase import Database

class Backend:
    def __init__(self):
        self.url = 'https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions'

    def parse(self):
        clist = {}
        source = requests.get(self.url).text
        soup = BeautifulSoup(source, 'lxml')
        table = soup.find('table',class_='wikitable sortable')
        tablehead = table.find('tbody')
        row = tablehead.find_all('tr')[5:]

        dt = pd.read_html(self.url,attrs={'class':''})
        print(dt)
        return clist






