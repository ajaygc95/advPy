from collections import defaultdict, namedtuple
import re


class Temperature:
    def __init__(self, item):
        self.item = item
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

    def __str__(self):
        for key, value in self.data_dict.items():
            if key == self.item:
                year = key
                value = [x.Median for x in value]
                return ("The median value of the year {} is {} :".format(year, "".join(value)))


temperature = Temperature('1852')
temperature.readdata('temperature.csv')
print(temperature)




