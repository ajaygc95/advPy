from AnnualTemperature import AnnualTemperature
from DataBase import Database
from Frontend import Frontend

if __name__ == "__main__":

    at = AnnualTemperature()
    data = at.openfile('Temperature.html')
    dt = Database()
    dt.createTable()
    for items in data:
        if len(items) > 0 and int(items[0]) > 1959 and int(items[0]) < 1991:
            dt.insert(items[0], items[2])
    frontend = Frontend()
    data = dt.get_all()
    x = []
    y = []

    for row in data:
        x.append(row[0])
        y.append(row[1])

    frontend.selectgraph(x, y)
    dt.delete_all_rows()
