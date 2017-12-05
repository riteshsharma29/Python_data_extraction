#!/usr/bin/python
# coding: utf-8 -*-

#This example shows reading a dataset using csv reader

import csv

#creating an empty list
MonthlySales = []

with open('data/MonthlySales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        MonthlySales.append(row)

for a in MonthlySales:
    print a

#print keys
for a in MonthlySales:
    print a.keys()

#print keys and values
for a in MonthlySales:
    for key, value in a.items():
        print key + ": ", value
    print '\n'
