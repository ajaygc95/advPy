from collections import defaultdict, namedtuple
import re


class SQLite(dict):
    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, item):
        return self.data[item]

    def readdata(self, filename):
        data_dict = {}
        clist = []
        with open(filename, 'r') as temp:
            lines = temp.readlines()[1:]
            for line in lines:
                data = re.findall(r'(?:,|\n|^)("(?:(?:"")*[^"]*)*"|[^",\n]*|(?:\n|$))', line)
                clist.append(data)
        for datum in clist:
            if datum[0] not in data_dict and len(datum) > 0:
                sqlite[int(datum[0])] = float(datum[2])



sqlite = SQLite()
sqlite.readdata('temperature.csv')
print(sqlite[1851])
