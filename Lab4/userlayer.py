__author__ = "Ajay GC"

from tkinter import *
from main import Scrape

from business import Business
from graphic import Graph

class UserLayer:
    def __init__(self):
        self.window = Tk()
    def drop_down(self):
        self.window.geometry("500x500")
        self.window.title("Choose Country to Graph ..")
        Label(text="").pack()
        Label(text="Select Country").pack()
        Label(text="").pack()
        scrape = Scrape()
        list1 = scrape.data_list()
        print(list1)
        clicked = StringVar()
        clicked.set(list1[0])
        drop = OptionMenu(self.window, clicked, *list1, command=self.selecter)
        drop.pack()
        self.window.mainloop()

    def selecter(self, event):
        Label(text=f"Country selected {event}").pack()
        return event
        # business = Business()
        # business.countryData(event)
        # graph = Graph()
        # graph.plotGraph(event)

