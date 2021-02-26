import sqlite3
from namedTuple import Temperature
from matplotlib import pyplot as plt

class Database:

    def createTable(self):
        try:
            conn = sqlite3.connect('midterm.db')
        except sqlite3.Error as e:
            print("Database connection failed due to : " + e)

        cur = conn.cursor()
        with conn:
            cur.execute('CREATE TABLE IF NOT EXISTS midterm (year int , temperature float)')

        temperature = Temperature()
        temperature.readdata('temperature.csv')
        temp_data = temperature.returndata()

        # for key, value in temp_data.items():
        #     year = key
        #     value = float(''.join([x.Median for x in value]))
        #
        #     cur.execute("INSERT INTO midterm VALUES(:year, :change)", {'year': year, 'change': value})
        #     conn.commit()
        # cur.close()


        # with conn:
        #     cur.execute('DROP TABLE midterm')
        #
        cur.execute('SELECT * FROM midterm')
        rows = cur.fetchall()
        year_list = []
        median_list = []
        for year,median in rows:
            year_list.append(year)
            median_list.append(median)

        plt.plot(year_list,median_list)
        plt.xlabel('Year')
        plt.ylabel('Change in Temperature')
        plt.title('Temperature change by year')
        plt.legend('Change')
        plt.show()



dt = Database()
dt.createTable()


