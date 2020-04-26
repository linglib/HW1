# -*- coding: utf-8 -*-
import lxml.etree as etree
import pandas as pd
import csv
import xml.etree.ElementTree as ET
from xml.dom import minidom

csvFile = r'/Users/linglibao/Downloads/ucla subject materials/ucla term 3 data management/hw1/FoodServiceData.csv'
csvData = csv.DictReader(open(csvFile))


# INITIALIZING XML FILE
root = etree.Element('foodservices')


# WRITE INITIAL XML NODES
for row in csvData:
    surface_elem = etree.SubElement(root, "foodservice")
    for elem_name, elem_value in row.items():
        etree.SubElement(surface_elem, elem_name.strip()).text = str(elem_value)


# WRITE OUTPUT TO FILE
tree = etree.ElementTree(root)


xmlstr = minidom.parseString(ET.tostring(root)).toprettyxml(indent="   ")
with open("/Users/linglibao/Downloads/ucla subject materials/ucla term 3 data management/hw1/FoodServiceData.xml", "w") as f:
    f.write(xmlstr)


