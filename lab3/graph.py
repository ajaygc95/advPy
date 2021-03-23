__author__ = "Ajay GC"

import sqlite3
import threading
from threading import Lock
import time
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

from database import Database
from Scraping import Scrape

plt.style.use('seaborn')

class Graph:
    def __init__(self):
        self.threads = {}

    def thread_read(self, key, lock):
        """Using context locking  ---WITH---"""
        with lock:
            read_database = Database()
            years = []
            values = []
            for year in range(1979, 2019):
                data = read_database.get_value(key, year)
                years.append(year)
                values.append(data[0][0])

            self.threads[key] = [years, value]

    def plotlinear(self, a, b, key):
        model = LinearRegression()
        x_value = np.array(a).reshape(-1, 1)
        y_value = np.array(b)

        final = model.fit(x_value, y_value)
        prediction = model.predict(x_value)
        plt.xlabel('Year')
        plt.ylabel(f'{str(key)} equivalent mixing ratio (ppm) ')
        plt.title(f'{str(key)} change by year')

        plt.scatter(a, b, color='green',edgecolors='aqua', label='Scatter plot')
        plt.plot(x_value, prediction, color='red', label='Linear Regression')
        plt.legend(loc='upper left')
        plt.show()
        print(final.score(x_value, y_value))

    def multiplePLot(self, a, b):
        plt.subplot(1, 3, 1)

if __name__ == "__main__":
    scrape = Scrape()
    scrape.parse()
    database = Database()
    database.createTable()
    graph = Graph()
    lock = Lock()
    columns = ['CO2', 'CH4', 'N2O', 'CFC12', 'CFC11', 'minor15']
    thread_list = []
    for col in columns:
        t = threading.Thread(target=graph.thread_read, args=(col, lock))
        t.start()
        thread_list.append(t)

    for th in thread_list:
        th.join()

    for item,value in graph.threads.items():
        graph.plotlinear(value[0],value[1],item)

    database.delete_all_rows()

