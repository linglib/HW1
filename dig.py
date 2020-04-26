# -*- coding: utf-8 -*-
from lxml import etree as et
import pandas as pd
import numpy as np


#READ BOOK.HTML FILE
with open ("/Users/linglibao/Downloads/ucla subject materials/ucla term 3 data management/hw1/book.html",encoding="utf-8") as f:
    f = f.read()
data = et.HTML(f)


#CREATE A LIST OF BOOK NAMES
list_name = data.xpath("body//div[@class='AllEditionsItem-tileTitle']/a/text()")
list_name = pd.Series(list_name)
list_name


#CREATE A LIST OF AUTHORS
list_author_raw=data.xpath("body//div[@class='SearchResultListItem-bottomSpacing SearchResultListItem-subheading']")
list_author = []


#IMPROVE THE LIST OF AUTHORS
for element in list_author_raw:
    if len(element)!=0:
        list_author.append(element.getchildren()[0].text)
    else:
        list_author.append("None")
list_author = pd.Series(list_author)


#CREATE A LIST OF DATA POINTS
list_datapoint = data.xpath("//div[@class = 'SearchResultTileItem-dataPoints']")


#CREATE A LIST OF CONDITION
list_condition = []
for element in list_datapoint:
    if len(element.xpath(".//div[@class='SearchResultListItem-subheading SearchResultListItem-bottomSpacing-small']/strong/text()")) !=0:
        list_condition.append(element.xpath(".//div[@class='SearchResultListItem-subheading SearchResultListItem-bottomSpacing-small']/strong/text()")[0])
    else:
        list_condition.append("None")
list_condition= pd.Series(list_condition)


#CREATE A LIST OF PRICE
list_price = []
for element in list_datapoint:
    if len(element.xpath(".//div[@class='SearchResultListItem-dollarAmount']/text()")) !=0:
        list_price.append(element.xpath(".//div[@class='SearchResultListItem-dollarAmount']/text()")[0])
    else:
        list_price.append("None")
list_price = pd.Series(list_price)


#CREATE ALIST OF FORMAT
list_format = []
for element in list_datapoint:
    if len(element.xpath(".//div[@class='SearchResultTileItem-format']/strong")) !=0:
        list_format.append(element.xpath(".//div[@class='SearchResultTileItem-format']/strong/text()")[0])
    else:
        list_format.append("None")
list_format = pd.Series(list_format)


#COMBINE ALL THE LISTS ABOVE INTO A DATA FRAME
df1 = pd.concat([list_name,list_author,list_condition,list_format,list_price],axis=1)
df1.columns = ['Name','Author','Condition','Format','Price']
df1["Condition"] = np.where(df1.Condition == "None","Temporarily Unavailable",df1.Condition)


#WRITE THE DATA FRAME INTO A XML FILE
xmlroot = et.Element("books")
for row in df1.to_dict(orient="records"):
    currentbook = et.SubElement(xmlroot,"book")
    for element,text in row.items():
        element_=et.SubElement(currentbook,element)
        element_.text = str(text)
with open(r'/Users/linglibao/Downloads/ucla subject materials/ucla term 3 data management/hw1/book.xml', 'wb') as f:
    f.write(et.tostring(xmlroot, pretty_print=True))



