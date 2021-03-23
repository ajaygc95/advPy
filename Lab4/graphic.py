__author__ = "Ajay GC"
from matplotlib import pyplot as plt
import numpy as np
import json
class Graph:
    def plotGraph(self,country):
        x = []
        y = []
        with open('json_data.json',"r") as read_file:
            data = json.load(read_file)
            for item in data:
                x.append(item[0])
                y.append(item[1])
        plt.plot(x, y,label=f'{country}')
        plt.xlabel('Year')
        plt.ylabel(f'Change in Temperature')
        # plt.title('Temperature change by year')
        plt.title(f'{str(country)}')
        plt.legend(loc='upper left')
        plt.show()
