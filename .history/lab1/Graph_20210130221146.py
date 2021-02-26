from matplotlib import pyplot as plt

class Graph:
    def __init__(self) -> None:
        self.plot = plt
    
    def plotGraph(self, x, y):
        plt.plot(x,y)
        plt.xlabel('Year')
        plt.ylabel('Change in Temperature')
        plt.title('Temperature change by year')
        plt.legend('Change')
        plt.show()

    def plotlinear(self,x,y):
        plt.plot