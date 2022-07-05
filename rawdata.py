# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:16:32 2021
NOUSE
@author: 15991
"""

import xlsxwriter

#open and read contents in txt
fopen = open("cleaned.txt",'r',encoding = 'utf-8')
lines = fopen.readlines()

#open an excel spreadsheet
workbook = xlsxwriter.Workbook('rawdata.xls')
worksheet = workbook.add_worksheet('data')


#write contents from txt to spreadsheet under four colums "recipe" "Amount" "Unit" "Ingredient"
i = 1
for line in lines:
    worksheet.write(i,0,line)
    i += 1

print(i)
#close the spreadsheet
workbook.close()