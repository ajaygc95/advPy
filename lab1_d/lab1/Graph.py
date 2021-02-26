from matplotlib import pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

class Graph:
    def __init__(self) -> None:
        self.plot = plt
    
    def plotGraph(self, x, y):
        plt.plot(x,y,label="Temp in Celcius")
        plt.xlabel('Year')
        plt.ylabel('Change in Temperature')
        plt.title('Temperature change by year')
        plt.legend()
        plt.show()

    def plotlinear(self,a,b):
        model = LinearRegression()
        x_value = np.array(a).reshape(-1,1)
        y_value = np.array(b)
        model.fit(x_value,y_value)
        prediction = model.predict(x_value)
        plt.xlabel('Year')
        plt.ylabel('Change in Temperature')
        plt.title('Temperature change by year')
        plt.scatter(a,b,label="Scatter data")
        plt.plot(x_value, prediction, color='red',label='Liner Regression')
        plt.legend()
        plt.show()

    def plotBar(self,x,y):
        plt.bar(x,y,label='Temp change in Celcius')
        plt.xlabel('Year')
        plt.ylabel('Change in Temperature')
        plt.title('Temperature change by year')
        plt.legend()
        plt.show()

