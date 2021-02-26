import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('country.db')
        self.c = self.conn.cursor()
    
    def createTable(self):
        with self.conn:
            self.c.execute('CREATE TABLE IF NOT EXISTS country (country char , percentage float)')

    def insert(self, country, percentage):
        with self.conn:
            self.c.execute("INSERT INTO country VALUES(:country, :percentage)",{'country':country,'percentage':percentage})
    
    def get_value(self,year):
        self.c.execute('SELECT * FROM country WHERE year=:year',{'year':year})
        return self.c.fetchall()

    def delete(self,year):
        with self.conn:
            self.c.execute('DELETE * from country WHERE year=:year',{'year':year})
    
    def delete_all_rows(self):
        with self.conn:
            self.c.execute('DROP TABLE country')

    def get_all(self):
        self.c.execute('SELECT * FROM country')
        rows = self.c.fetchall()
        return rows

