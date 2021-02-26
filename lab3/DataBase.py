import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('country.db')
        self.c = self.conn.cursor()

    def createTable(self):
        with self.conn:
            self.c.execute(
                'CREATE TABLE IF NOT EXISTS country (year int , CO2 float, CH4 float, N2O float, CFC12 float, '
                'CFC11 float, minor15 float )')

    def insert(self, a, b, c, d, e, f, g):
        with self.conn:
            self.c.execute("INSERT INTO country VALUES(:year, :CO2, :CH4, :N2O, :CFC12, :CFC11, :minor15)",
                           {'year': a, 'CO2': b, 'CH4': c, 'N2O': d, 'CFC12': e, 'CFC11': f, 'minor15': g})

    def get_value(self, item, year):
        self.c.execute(f'SELECT {item} FROM country WHERE year={year}')
        return self.c.fetchall()

    def delete(self, year):
        with self.conn:
            self.c.execute('DELETE * from country WHERE year=:year', {'year': year})

    def delete_all_rows(self):
        with self.conn:
            self.c.execute('DROP TABLE country')

    def get_all(self):
        self.c.execute('SELECT * FROM country')
        rows = self.c.fetchall()
        return rows
