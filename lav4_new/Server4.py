import socket
from main import Scrape
import pickle
from database import Database
from business import Business

# Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = socket.gethostname()   # Get local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print('Server listening....')

while True:
    conn, addr = s.accept()     # Establish connection with client.
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))
    scrape = Scrape()
    scrape.data_list()
    business = Business()
    country_data = business.countryData(data)
    l = pickle.dumps(country_data)


    # filename='dog.jpg' #In the same folder or path is this file running must the file you want to tranfser to be
    # f = open(filename,'rb')
    # l = f.read(1024)

    while (l):
        conn.send(l)
        print('Sent ',repr(l))
        l = f.read(1024)

    print('Done sending')
    conn.close()