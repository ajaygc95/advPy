__author__ = "Ajay GC"
import json
import xml.etree.cElementTree as e
def json_to_xml():


    with open('output.json') as read_json:
        data = json.load(read_json)
        r = e.Element("Presidents")
        for item, value in data.items():
            e.SubElement(r, 'Rank').text = item
            e.SubElement(r, 'Name').text = value
            a = e.ElementTree(r)
        a.write("president.xml")

json_to_xml()