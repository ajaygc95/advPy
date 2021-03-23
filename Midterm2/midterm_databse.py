import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('president.db')
        self.c = self.conn.cursor()

    def createTable(self):
        with self.conn:
            self.c.execute(
                'CREATE TABLE IF NOT EXISTS country (Rank int , Name char )')

    def insert(self, a, b):
        with self.conn:
            self.c.execute("INSERT INTO country VALUES(:Rank, :Name)",
                           {'Rank': a, 'Name': b})

    # def get_value(self, item, year):
    #     self.c.execute(f'SELECT {item} FROM country WHERE year={year}')
    #     return self.c.fetchall()
    #
    # def delete(self, year):
    #     with self.conn:
    #         self.c.execute('DELETE * from country WHERE year=:year', {'year': year})
    #
    def delete_all_rows(self):
        with self.conn:
            self.c.execute('DROP TABLE country')

    # def get_all(self):
    #     self.c.execute('SELECT * FROM country')
    #     rows = self.c.fetchall()
    #     return rows
