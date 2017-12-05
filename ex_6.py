#!/usr/bin/python
# coding: utf-8 -*-

#This example shows few quicks ways to load complex json datasets using pandas

import json
from pandas.io.json import json_normalize
import pandas as pd
import sys


with open('data/monthlySalesbyCategoryMultiple.json') as json_data:
    d = json.load(json_data)

jdf = json_normalize(d['contents'], 'monthlySales', ['category', 'region'])

jdf

df = pd.read_csv('data/MonthlyProductSales.csv')

# show first 10 rows
df.head(n=10)

# show last 10 rows
df.tail(n=10)

# show summary stats of the sales column
df.describe()

df.info()

# return as a series
s = df['Product Name']

# get count of values
s.value_counts(dropna=False)

print df['Month of Order Date'].str[:4]

# yearly sales summary
yearly_sales = df.groupby(df['Month of Order Date'].str[:4]).describe().reset_index().rename(columns={'Month of Order Date': 'Year of Order'})

# yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
df_export.rename(columns={'Month of Order Date': 'Year of Order'})

# overall product sales totals
df.groupby('Product Name').sum().reset_index()
