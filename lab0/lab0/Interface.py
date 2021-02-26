
from collections import defaultdict
from Database import Database

class Interface:
    def __init__(self,filename):
        self.filename = filename
    
    def filtercarbondata(self):
        newdict = defaultdict()
        
        DB = Database(self.filename)
        db = DB.dataStoreCarbon()
        for key,value in db.items():
            dict1 = {}           
            for val in value:        
                dictvalue = 0
                count = 0
                if val[0] == key:
                    dictvalue += float(val[3])
                    count += 1
         
                dict1['total_ave'] = dictvalue
                newdict[key] = dict1
        return newdict

    def filterAnnualtemperature(self):        
        DB = Database(self.filename)
        db = DB.dataStoreTemp()

        return db