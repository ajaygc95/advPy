__author__ = "Ajay GC"

from collections import defaultdict, namedtuple
import re


class Temperature:
    def __init__(self):
        self.data_dict = defaultdict(list)

    def readdata(self, filename):
        clist = []
        with open(filename, 'r') as temp:
            lines = temp.readlines()[1:]
            for line in lines:
                data = re.findall(r'(?:,|\n|^)("(?:(?:"")*[^"]*)*"|[^",\n]*|(?:\n|$))', line)
                clist.append(data)

        annualtemp = namedtuple("Temp", ["year", "Median", "Upper", "Lower"])
        
        for datum in clist:
            self.data_dict[datum[0]].append(annualtemp(datum[0], datum[1], datum[2], datum[3]))

    def returndata(self):
        return self.data_dict


if __name__ == '__main__' :
    temp = Temperature()
    temp.readdata('temperature.csv')
    output = temp.returndata()

    for data,value in output.items():
        print(value)