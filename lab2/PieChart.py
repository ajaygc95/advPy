__author__ = "Ajay GC"

from backend_lab2 import Backend
from matplotlib import pyplot as plt
from DataBase import Database

class PieChart:
    def __init__(self):
        self.Backend = Backend()
        self.database = Database()
        self.sorted_data = {}

    def send_data(self):
        self.database.createTable()
        for key, value in self.Backend.parse().items():
            self.database.insert(key, value)

    def get_data(self):
        database = Database()
        data = database.get_all()
        for key, value in data:
            self.sorted_data[key] = value
        return self.sorted_data

    def pie_chart(self, data):
        count = 0
        percentage = []
        country = []
        explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        for cntry, pnt in data.items():
            if count < 10 and cntry != "European Union":
                percentage.append(pnt)
                country.append(cntry)
                count += 1

        plt.pie(
            percentage, labels=country,
            wedgeprops={'edgecolor': 'white'},
            # autopct=lambda percentage: f'{percentage:.2f}%',
            autopct='%1.1f%%',
            shadow=True,
            explode=explode
        )
        plt.title("Top 10 Country by C02 Emission In 2017")
        plt.axis('equal')
        plt.show()


if __name__ == '__main__':
    graph = PieChart()
    graph.send_data()
    database = Database()
    data = graph.get_data()
    final_sort = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    graph.pie_chart(final_sort)
    database.delete_all_rows()
