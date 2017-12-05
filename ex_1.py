#!/usr/bin/python
# coding: utf-8 -*-

#This is a interesting example which shows reading a json dataset

import json
from pprint import pprint as pp

# load json file from /data folder usinh with handle
with open('data/monthlySalesbyCategoryMultiple.json') as json_data:
    d = json.load(json_data)

# see what the dictionary looks like
pp (d)

# print keys,values at the top level
print d.keys(),d.values()

# print keys at the second level
for a in d['contents']:
    print a.keys()

# print keys at the third level
for a in d['contents']:
    for b in a['monthlySales']:
        print b.keys()

# print the keys and values at the first level
for key, value in d.items():
    print key + ': ', pp(value)

# print the keys and values at the second level
for a in d['contents']:
    for key, value in a.items():
        print key + ': ', value

# print the keys and values at the third level
for a in d['contents']:
    for b in a['monthlySales']:
        for key, value in b.items():
            print key + ": ", value
