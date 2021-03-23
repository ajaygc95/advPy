__author__ = "Ajay GC"

from midterm_databse import Database
import json
import threading
from threading import Lock

class ThreadDatabase:

    def send_to_database(self, rank,name, lock):
        with lock:
            self.database = Database()
            self.database.createTable()
            self.database.insert(rank,name)

if __name__ == "__main__":
    thread_list = []
    with open('output.json') as read_json:
        data = json.load(read_json)

        lock = Lock()
        thread_db = ThreadDatabase()
        for item,value in data.items():
            t = threading.Thread(target=thread_db.send_to_database, args=(item,value,lock))
            t.start()
            thread_list.append(t)

        for th in thread_list:
            th.join()

        # Database().delete_all_rows()

