__author__ = "Ajay GC"

import sqlite3
import threading
from threading import Lock
import time
from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

from database import Database

class Graph:
    def __init__(self):
        self.threads = {}

    def plotGraph(self, key, lock):
        with lock:
            database = Database()
            years = []
            value = []
            for year in range(1980,2019):
                data = database.get_value(key,year)
                years.append(year)
                value.append(data[0][0])

            self.threads[key] = [years,value]

    def plotlinear(self, a, b, key):
        model = LinearRegression()
        x_value = np.array(a).reshape(-1, 1)
        y_value = np.array(b)

        final = model.fit(x_value, y_value)
        prediction = model.predict(x_value)
        plt.xlabel('Year')
        plt.ylabel('Change in Temperature')
        plt.title(f'Temperature change by year {str(key)}')
        plt.scatter(a, b)
        plt.plot(x_value, prediction)
        plt.show()

        print(final.score(x_value, y_value))


if __name__ == "__main__":
    starttime1 = time.time()
    graph = Graph()
    lock = Lock()
    columns = ['CO2', 'CH4', 'N2O', 'CFC12', 'CFC11', 'minor15']
    thread_list = []
    for col in columns:
        t = threading.Thread(target=graph.plotGraph, args=(col,lock))
        t.start()
        thread_list.append(t)

    for th in thread_list:
        th.join()

    print(thread_list)
    for item,value in graph.threads.items():
        graph.plotlinear(value[0],value[1],item)


