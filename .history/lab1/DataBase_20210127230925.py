import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('temperature.db')
        self.c = self.conn.cursor()
    
    def createTable(self):
        with self.conn:
            self.c.execute('CREATE TABLE IF NOT EXITS temperature (year int , temperature float)')

    def create(self, year, change):
        with self.conn:
            self.c.execute("INSERT INTO temperature VALUES(:year, :change)",{'year':year,'change':change})
    
    def get_value(self,year):
        self.c.execute('SELECT * FROM temperature WHERE year=:year',{'year':year})
        return self.c.fetchall()

    def delete(self,year):
        with self.conn:
            self.c.execute('DELETE * from temperature WHERE year=:year',{'year':year})
    
    def delete_all_rows(self):
        with self.conn:
            self.c.execute('DROP TABLE temperature')


    def get_all(self):
        self.c.execute('SELECT * FROM temperature WHERE year > 1960 and year < 2018')
        rows = self.c.fetchall()
        return rows

dt = Database()
