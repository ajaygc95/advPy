__author__ = "Ajay GC"

# passowrd just in case mPLvDtCsUFNx
from bs4 import BeautifulSoup
import  json
from midterm_databse import Database
import xml.etree.cElementTree as e

with open('Presidents.html', 'r') as html_file:
    toprint = html_file
    soup = BeautifulSoup(toprint, 'lxml')
    table = soup.find('table', class_='table')
    row = table.find_all('tr')
    item_dict = {}
    for td in row[1:]:
        number = td.find_all('b')
        value = number[0].text
        rank = value.split()[0]
        name = value.split(None, 1)[1]
        item_dict[rank] = name


json_object = json.dumps(item_dict, indent = 4)
with open('output.json','w') as json_file:
    json.dump(item_dict, json_file)

def send_to_database():
    database = Database()
    database.createTable()

    with open('output.json') as read_json:
        data = json.load(read_json)

        for item,value in data.items():
            database.insert(item,value)

    # database.delete_all_rows()




    # database.delete_all_rows()