__author__ = "Ajay GC"

from tkinter import *
from main import Scrape

from business import Business
from graphic import Graph

class UserLayer:
    def __init__(self):
        self.value = None
        self.window = Tk()
    def drop_down(self):
        self.window.geometry("500x500")
        self.window.title("Choose Country to Graph ..")
        Label(text="").pack()
        Label(text="Select Country").pack()
        Label(text="").pack()
        scrape = Scrape()
        list1 = scrape.data_list()
        print(list1[:10])
        clicked = StringVar()
        clicked.set(list1[0])
        drop = OptionMenu(self.window, clicked, *list1[:10], command=self.selecter)
        drop.pack()
        self.window.mainloop()

    def selecter(self, event):
        Label(text=f"Country selected {event}").pack()
        print(": I am here")
        self.value = event
        self.func()
        return event

    def func(self):
        print(" I amin func")
        return self.value
        # business = Business()
        # business.countryData(event)
        # graph = Graph()
        # graph.plotGraph(event)

ui = UserLayer()
to_print = ui.drop_down()
print(ui.func())
