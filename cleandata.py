"""
By: Renjie Zhong

The program is used to clean invalid data in temp1.xls(contains recipe name, amount, unit and ingredidents)
This program mainly changed all invalid number in the amount column into valid data pattern

Package required to manually installed:
1. pip install xlrd
2. pip install xlutils

This program requires to run an existed file named "temp1.xls"
and will eventually create a new file named "clean1。xls"

"""

import xlrd
from xlutils.copy import copy

# load the excel file
rb = xlrd.open_workbook('temp1.xls')
 
# copy the contents of excel file
wb = copy(rb)
 
# open the first sheet
w_sheet = wb.get_sheet(0)
r_sheet = rb.sheet_by_name('data')



#inspect amount colums and convert incorrect format to double numbers
i = 7940
m = 1
for m in range(i):
    s = r_sheet.cell(m,1).value
    if "½" in s:
        s = "0.5"
        w_sheet.write(m,1,s)        
    if "¼" in s:
        s = "0.25"
        w_sheet.write(m,1,s)
    if "1-" == s:
        s = "1"
        w_sheet.write(m,1,s)
    if ("-" in s) and (s[-1] == "-"):
        s = s[:-1]
        if (" " in s) and ("/" not in s):
            s = s.split()
            s = (float(s[0]))*(float(s[1]))
        w_sheet.write(m,1,s)

for m in range(i):
    s = r_sheet.cell(m,1).value
    s = list(s)
    if "-" in s:
        index = s.index("-")
        s[index]=" "
        s=''.join(s)
        w_sheet.write(m,1,s)

for m in range(i):
    s = r_sheet.cell(m,1).value
    s = str(s)
    if "-1/2" in s:
        s = s.split()
        index = s.index("-1/2")
        s[index]=" 0.5 "
        w_sheet.write(m,1,s)

for m in range(i):
    s = r_sheet.cell(m,1).value
    s = str(s)
    if "1/2" in s:
        s = s.split()
        if "1/2" in s:
            index = s.index("1/2")
            s[index]=" 0.5 "
        w_sheet.write(m,1,s)
        
for m in range(i):
    s = r_sheet.cell(m,1).value
    s = str(s)
    if "1/3" in s:
        s = s.split(" ")
        if "1/3" in s:
            index = s.index("1/3")
            s[index]=" 0.3 "
        w_sheet.write(m,1,s)
        
for m in range(i):
    s = r_sheet.cell(m,1).value
    s = str(s)
    if "1/4" in s:
        s = s.split(" ")
        if "1/4" in s:
            index = s.index("1/4")
            s[index]=" 0.25 "
        w_sheet.write(m,1,s)

for m in range(i):
    s = r_sheet.cell(m,1).value
    s = str(s)
    if "2/3" in s:
        s = s.split(" ")
        if "2/3" in s:
            index = s.index("2/3")
            s[index]=" 0.6 "
        w_sheet.write(m,1,s)
        
for m in range(i):
    s = r_sheet.cell(m,1).value
    s = str(s)
    if "3/4" in s:
        s = s.split(" ")
        if "3/4" in s:
            index = s.index("3/4")
            s[index]=" 0.75 "
        w_sheet.write(m,1,s)

# save the file
wb.save('clean1.xls')