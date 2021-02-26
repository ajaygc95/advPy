from Graph import Graph
import re
from collections import namedtuple
from DataBase import Database
from Frontend import Frontend
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

