from Interface import Interface
from collections import defaultdict

class Process:
    def __init__(self):
        pass
    def processdata(self):
        dict1 = {}
        list1 = []

        CO2 = Interface("Co2.html")
        co2 = CO2.filtercarbondata()

        TEMP = Interface("Temperature.html")
        temp = TEMP.filterAnnualtemperature()
        for item, value in co2.items():
            if item not in dict1:
                for key,pair in value.items():
                    dict1[item] = {'year':item,'Average':pair}
                    list1.append([int(item),int(pair)])
      
        for item,value in temp.items():
            # ======= Compreshension =======
            res1 =any(int(item) in sublist for sublist in list1)
            for key in value:
                if res1 == True:
                    dict1[item]['change']= key[2]

        return dict1

if __name__ == "__main__":
    pr = Process()
    data = pr.processdata()
    print('-------------------------------')
    print(' year   |  Average  |  Temperature ')
    print('-------------------------------')
    for item,value in data.items():
        year1 = int(value['year'])
        if int(value['year'])<=2018:
            print(f" {value['year']}   |   {value['Average']:.2f}  |  {value['change']}        ")
    print('==============================')


        


