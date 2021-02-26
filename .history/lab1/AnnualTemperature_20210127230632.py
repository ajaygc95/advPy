from Graph import Graph
import re
from collections import namedtuple
from DataBase import Database
class AnnualTemperature:

    def __init__(self):
        pass

    def openfile(self, filename):
        clist = []
        with open(filename, "r") as fp:
            lines = fp.readlines()[5:]
            for line in lines: 
                #Regular expression to read HTML table data.            
                data = re.findall(r'(?i)<td.*?>([^<]+)</td.*?>', line)
                clist.append(data)
        return clist



if __name__ == "__main__":

    at = AnnualTemperature()
    data = at.openfile('lab1\Temperature.html')
    dt = Database()
    for items in data:
        dt.create(items[0],items[3])

   
    graph = Graph()

    # dt.create()
    # data = dt.get_all()
    # x = []
    # y = []

    # for row in data:
    #     x.append(row[0])
    #     y.append(row[1])

    # graph.plotGraph(x,y)

    # dt.delete_all_rows()
        
        

                