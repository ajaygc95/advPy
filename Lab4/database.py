__author__ = "Ajay GC"
import sqlite3
class Database:
    def __init__(self):
        self.conn = sqlite3.connect('country_data_UN.db')
        self.c = self.conn.cursor()

    def createTable(self):
        with self.conn:
            self.c.execute(
                'CREATE TABLE IF NOT EXISTS country_table (country_table char, year int, value float)')

    def insert(self,country_table,year,value):
        with self.conn:
            self.c.execute("INSERT INTO country_table VALUES(:country_table, :year, :value)",
                           {'country_table': country_table, 'year':year, 'value': value})

    def get_value(self, country_table):
        self.c.execute(f'SELECT * FROM country_table WHERE country_table = "{country_table}" ')
        return self.c.fetchall()

    def delete(self, year):
        with self.conn:
            self.c.execute('DELETE * from country_table WHERE year=:year', {'year': year})

    def delete_all_rows(self):
        with self.conn:
            self.c.execute('DROP TABLE country_table')

    def get_all(self):
        self.c.execute('SELECT * FROM country_table')
        rows = self.c.fetchall()
        return rows
