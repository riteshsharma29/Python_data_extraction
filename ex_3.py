#!/usr/bin/python
# coding: utf-8 -*-

#This example shows reading a parquet file pyarrow

import pyarrow.parquet as pq

table = pq.read_table('data/MonthlyProductSales.parquet')

table_dict = dict(table.to_pydict())

# table dict is more of a columnar dictionary
table_dict

# going to convert it to a list of dictionaries
items = table_dict.items()
items

# get the keys
keys = [item[0] for item in items]
keys

# get the values
values = [item[1] for item in items]
values

# zip the values together
pivoted_values = zip(*values)
pivoted_values

# zip the column with the corresponding value then convert
# it to a dictionary then append it to an array
table_dictionary_array = []
for record in pivoted_values:
    table_dictionary_array.append(dict(zip(keys, record)))

for record in table_dictionary_array:
    print(record)
