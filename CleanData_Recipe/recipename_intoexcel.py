
"""
By: Renjie Zhong

This program is used to write txt file (scraping data) into xls file
There will be four columns in xls file, containing recipe's name, amount, unit and ingredient

Module required to be manually installed:
pip3 install xlsxwriter

This program needs to run an existed file named "recipe_name.txt"
and will create a new file named "recipe_name_raw.xls"
"""

import xlsxwriter

#open and read contents in txt
fopen = open("recipe_name.txt",'r',encoding = 'utf-8')
lines = fopen.readlines()

#open an excel spreadsheet
workbook = xlsxwriter.Workbook('recipe_name_raw.xls')
worksheet = workbook.add_worksheet('data')

#write headers
worksheet.write(0,0,"Recipe")
worksheet.write(0,1,"Amount")
worksheet.write(0,2,"Unit")
worksheet.write(0,3,"Ingredient")

#write contents from txt to spreadsheet under four colums "recipe" "Amount" "Unit" "Ingredient"
i = 1
for line in lines:
    str = line.split('\t')
    #delte headers in txt
    tempstr = str[0].split()
    if tempstr[0].strip()=="Recipe":
        continue

    n=0
    for s in str:
        worksheet.write(i,n,s)
        n += 1
        
    i += 1

print(i)
#close the spreadsheet
workbook.close()

