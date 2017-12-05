#!/usr/bin/python
# coding: utf-8 -*-

#This example shows reading a URL json & csv encoded with base64

import requests
import json
from pprint import pprint as pp
import csv
import io
import pandas as pd
import sys


response = requests.get('https://api.github.com/repos/bsullins/data/contents/monthlySalesbyCategoryMultiple.json')
resp_json = json.loads(response.text)

val = json.loads(resp_json['content'].decode('base64'))
#pp(val)


sales = []
month = []

# print the keys and values at the third level
for a in val['contents']:
    for b in a['monthlySales']:
        for key, value in b.items():
            if key == "sales":sales.append(value)
            if key == "month":month.append(value)

df_1 = pd.Series(sales)
df_2 = pd.Series(month)
df = pd.concat([df_1,df_2],axis=1)
df.columns = ['sales','month']

print df.head()

######################################################################################################################

response = requests.get('https://api.github.com/repos/bsullins/data/contents/MonthlySales.csv')

response_json = json.loads(response.text)

csv_val = response_json['content'].decode('base64')

# using csv.DictReader needs a filestream so we're making an String IO and passing a unicode string in
# then reading the stream and adding each dictionary to the dictionary list

csv_dict = csv.DictReader(io.StringIO(unicode(csv_val)))
dict_list = []
for a in csv_dict:
    dict_list.append(a)

df_2 = pd.DataFrame(dict_list)

print df_2



