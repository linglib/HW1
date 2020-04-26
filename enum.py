# -*- coding: utf-8 -*-
from lxml import etree as et
import pandas as pd


#READ XML FILE
data = et.parse("/Users/linglibao/Downloads/ucla subject materials/ucla term 3 data management/hw1/FoodServiceData.xml")
root = data.getroot()


#PUT ELEMENTS TAG INTO THE COLNAME LIST
colname=[]
for element in root[0]:
    colname.append(element.tag)


# CREATE AN EMPTY DICTIONARY AND EMPTY LISTS IN THE EMPTY DICTIONARY.
# EACH EMPTY LIST CORRESPONDS TO AN ELEMENT TAG
elemdict={}
for i in colname:
    elemdict[i]=[]


#STORE THE FEATURES OF EACH ELEMENT INTO THEIR CORRESPONDING LIST
for element in root:
    for i in colname:
        if element.find(i).text == 'nan':
            elemdict[i].append("None")
        else:
            elemdict[i].append(element.find(i).text)


#GROUP ALL THE ELEMENTS BY THEIR TYPE DESCRIPTION AND PRINT OUT THE GROUP SIZE
data=pd.DataFrame(elemdict)
group1 = data.groupby("TypeDescription")
print(group1.size())


#GROUP ALL THE ELEMENTS BY THEIR GRADE AND PRINT OUT THE GROUP SIZE
group2 = data.groupby("Grade")
print(group2.size())




