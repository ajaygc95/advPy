__author__ = "Ajay GC"

import socket
from main import Scrape
import pickle
from business import Business


class Server:
    def __init__(self, port):
        self.host = socket.gethostname()
        self.port = port  # initiate port no above 1024
        self.server_socket = socket.socket()  # get instance
        self.server_socket.bind((self.host, self.port))  # bin
        self.HEADERSIZE = 10

    def read_data(self):
        filename = 'UNData.xml'  # In the same folder or path is this file running must the file you want to tranfser to be
        f = open(filename, 'rb')
        l = f.read(1024)

    def Connect(self):
        # configure how many client the server can listen simultaneously
        print("server is started and listening on port >>>>>>>>", self.port)
        self.server_socket.listen(5)
        conn, address = self.server_socket.accept()
        print("Connection from: " + str(address))

        while True:
            print("Looping while loop")
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("Country Selected : ", data)
            scrape = Scrape()
            scrape.data_list()
            business = Business()
            country_data = business.countryData(data)
            print(type(country_data))
            msg = pickle.dumps(country_data)
            print("done pickling")
            conn.send(msg)
            print("DATA SENT TO THE CLIENT.... ")


if __name__ == '__main__':
    server = Server(5000)
    server.Connect()
