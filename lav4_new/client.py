__author__ = "Ajay GC"

import socket
import pickle
import json
from matplotlib import pyplot as plt
from graphic import Graph
from ui import UserLayer

class Client:
    def __init__(self, nport):
        self.host = socket.gethostname()  # as both code is running on same pc
        self.port = nport  # socket server port number
        self.client_socket = socket.socket()  # instantiate
        self.client_socket.connect((self.host, self.port))  # connect to the server
        self.HEADERSIZE = 10
        self.final_data = None
        self.country_name = ""

    def Connect(self, country_name):
        self.country_name = country_name
        while country_name.lower() != 'quit':
            self.client_socket.send(country_name.encode())  # send message
            print('receiving data...')
            data = self.client_socket.recv(1024)
            # print('data=%s', (data))
            to_print = pickle.loads(data)
            self.final_data = to_print
            country_name = 'quit'
        self.client_socket.close()

    def graph(self):
        x = []
        y = []

        graph_data = json.loads(self.final_data)
        sorted_data = sorted(graph_data.items(), key=lambda x: x[0])
        print(type(sorted_data))
        for item, value in sorted_data:
            x.append(item)
            y.append(value)

        print(sorted_data)
        print(x)
        print(y)

        graph = Graph()
        graph.plotGraph(x,y,self.country_name)


if __name__ == '__main__':
    ui = UserLayer()
    country_name = ui.drop_down()
    print(country_name)

    # country_name = ui.sel_ctry
    # print("pritned from client",country_name)
    # client = Client(5000)
    # client.Connect(country_name)
    # client.graph()
