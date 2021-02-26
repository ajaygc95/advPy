from collections import defaultdict, namedtuple
class Temperature:
    def __init__(self):
        self.data = defaultdict()
    
    def readdata(self,filename):
        with open(filename, 'r') as temp:
            for item in temp:
                print(item)

        
temperature = Temperature()
temperature.readdata()