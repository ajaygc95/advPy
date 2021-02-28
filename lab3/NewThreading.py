__author__ = "Ajay GC"

import threading
from database import Database

class Graph:
    def __init__(self):
        self.threads = []
        self.data_item = ['CO2','CHR','N20','CFC12','CFC11','minor15']

    def read_data(self):
        for item in self.data_item:
            t = threading.Thread(target=some_finction,args=[item])
            t.start()
            self.threads.append(t)


    def after_main(self):
        for thread in self.threads:
            thread.join()
