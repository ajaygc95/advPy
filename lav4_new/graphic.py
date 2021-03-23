__author__ = "Ajay GC"
from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
import numpy as np
import json
class Graph:

    def plotGraph(self,x,y,country):
        plt.plot(x, y,label=f'{country}')
        plt.xlabel('Year')
        plt.ylabel(f'Change in Temperature')
        # plt.title('Temperature change by year')
        plt.title(f'{str(country)}')
        plt.legend(loc='upper left')
        plt.gca().xaxis.set_major_locator(MaxNLocator(prune='lower'))
        plt.show()
