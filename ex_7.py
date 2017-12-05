#!/usr/bin/python
# coding: utf-8 -*-

#This example shows extracting dataframe analysis report to various export formats

import json
from pandas.io.json import json_normalize
import pandas as pd
import sys

df = pd.read_csv('data/MonthlyProductSales.csv',encoding='cp1252')

# yearly product sales totals
df_export = df.groupby([df['Month of Order Date'].str[:4], 'Product Name']).sum().reset_index()
df_export.rename(columns={'Month of Order Date': 'Year of Order'})

# export to csv, check csv when finished
df_export.to_csv('data/output/YearlyProductSalesTotals.csv', header=True, index=False, encoding='utf-8')

# export to json, check json when finished
df_export.to_json('data/output/YearlyProductSalesTotals.json', orient='records')

# export to excel, check excel file when finished
df_export.to_excel('data/output/YearlyProductSalesTotals.xlsx', header=True, index=False)
