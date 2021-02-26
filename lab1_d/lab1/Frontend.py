from tkinter import *
from Graph import Graph

class Frontend(object):
    def __init__(self):
        self.window = Tk()
        print("======= Graph =======")

    def selectgraph1(self, x, y):
        '''Tkinter GUI 1'''
        frame = Frame(self.window, width=500, height=500)
        # label1 = tk.Label(self.window,text="HEllO")
        # label2 = tk.Label(self.window,text="WORLD")
        button1 = Button(self.window, text="Plot line", padx=50)
        button2 = Button(self.window, text="Linear Regression", padx=50)
        # button3 = tk.Button(self.window, text="Bar Graph", padx=50, command=self.plotbar(x, y))
        # button1.grid(row=0,column=0)
        # button2.grid(row=1,column=0)
        # button1.pack()
        button1.bind('<Button-1>')
        button1.grid(row=0, sticky='w')

        button2.bind("<Button-1>")
        button2.grid(row=1, sticky='w')
        frame.grid(row=2)
        self.window.mainloop()

    def selectgraph(self,x,y):
        '''Tkinter GUI 1'''
        self.window.geometry("500x500")
        self.window.title("Year by Year Temperature Data")
        Label(text="").pack()
        Label(text = "Select Graph of your choice from options below").pack()
        Label(text="").pack()
        Button(text='XY Plot',height ="2",width="30",command=lambda : self.plotline(x,y)).pack()
        Label(text="").pack()
        Button(text='Linear Regression ',height ="2",width="30",command=lambda : self.plotlinear(x,y)).pack()
        Label(text="").pack()
        Button(text='Bar Chart',height ="2",width="30",command=lambda : self.plotbar(x,y)).pack()

        Label(text="").pack()
        Label(text = "NOTE: ").pack()
        Label(text = "You can close the graph window and choose another option ").pack()

        self.window.mainloop()


    def plotline(self,*args):
        graph = Graph()
        graph.plotGraph(*args)

    def plotlinear(self,*args):
        graph = Graph()
        graph.plotlinear(*args)

    def plotbar(self,*args):
        graph = Graph()
        graph.plotBar(*args)
