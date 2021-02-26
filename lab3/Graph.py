__author__ = "Ajay GC"

import sqlite3
import threading
from threading import Lock
import time

from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

from DataBase import Database

class Graph:
    def __init__(self):
        self.database = Database()

    def plotGraph(self, key, lock):
        with lock:
            years = []
            value = []
            for year in range(1980,2019):
                data = self.database.get_value(key,year)
                years.append(year)
                value.append(data[0][0])

            self.plotlinear(years,value,key)

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
    t1 = threading.Thread(target=graph.plotGraph, args=('CO2', lock))
    t2 = threading.Thread(target=graph.plotGraph, args=('CH4', lock))
    t3 = threading.Thread(target=graph.plotGraph, args=('N2O', lock))
    t4 = threading.Thread(target=graph.plotGraph, args=('CFC12', lock))
    t5 = threading.Thread(target=graph.plotGraph, args=('CFC11', lock))
    t6 = threading.Thread(target=graph.plotGraph, args=('minor15', lock))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()

    print(time.time()-starttime1)


