from collections import defaultdict, namedtuple
class Temperature:
    def __init__(self):
        self.data = defaultdict()
    
    def readdata(self):
        with open('lab1_d\lab1\exam\temperature.csv','r') as temp:
            for item in temp:
                print(item)

        
temperature = Temperature()
temperature.readdata()