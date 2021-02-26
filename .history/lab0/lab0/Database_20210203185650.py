from collections import namedtuple, defaultdict
from CarbonEmission import CarbonEmission
from AnnualTemperature import AnnualTemperature

class Database:
    def __init__(self, openFile):
        self.openFile = openFile

    def dataStoreCarbon(self):

        #======== Defaultdict ===========
        dates_dict = defaultdict(list)

        #======== NamedTuple ===========
        stu = namedtuple("Data",["year", "month","decimal","average","interpolated","trend","days"])
        CE = CarbonEmission()
        data = CE.openfile(self.openFile)
        for datum in data:
            if len(datum) != 0 and len(datum) == 7:
                dates_dict[datum[0]].append(stu(datum[0],datum[1],datum[2],datum[3],datum[4],datum[5],datum[6] ))
        return dates_dict  

    def dataStoreTemp(self):
        #======== Defaultdict ===========
        dates_dict = defaultdict(list)

        #NamedTuple
        annualtemp = namedtuple("Grade",["year", "Median","Upper","Lower"])
        AT = AnnualTemperature()
        data = AT.openfile(self.openFile)
        for datum in data:
            if len(datum) != 0 and len(datum) == 4:
                dates_dict[datum[0]].append(annualtemp(datum[0],datum[1],datum[2],datum[3]))
        return dates_dict


# 