excel spreedsheet
-- for this download openpyxl

import openpyxl as xl  # here istead calling package namge evry time we can assign values
wb = xl.load_workbook('transaction.xlsx')      #here we are loading the excel

#call the sheet
sheet = wb["Sheet1"]          #sheet name shld be as per in the excel

#how to call rows & columns
cell = sheet["a1"]          #calling directly cell name
# 'or'
cell = sheet.cell(1,1)      #calling row and column number

#how to print number of rows

for row in sheet(1 ,sheet.max_row + 1):             #(1,4) prints only 1,2,3 so we are using +1
    print(row)

#If i want to ignore 1st heading rows and get only tht column values
for row in sheet(2 ,sheet.max_row + 1):             #(1,4) prints only 1,2,3 so we are using +1
    cell = sheet.cell(row,3)            #3 is column
    print(cell.value)             #this prints the values frm tht column

#If i want crt tht price column
for row in sheet(2 ,sheet.max_row + 1):             #(1,4) prints only 1,2,3 so we are using +1
    cell = sheet.cell(row,3)
    corrected_Cell = cell.value * 0.9
    print(corrected_Cell)

#if i want to save the correct row values in differnt column
for row in sheet(2 ,sheet.max_row + 1):
    cell = sheet.cell(row,3)
    corrected_Cell = cell.value * 0.9
    corrected_Cell_row = sheet.cell(row,4)      #in 4th column values of the correct will be printed
    corrected_Cell_row.value = corrected_Cell

wb.save("tranaction2.xlsx")     #This create another excel without changing the original excel

-==How to create charts==========

from openpyxl.chart import BarChart,Reference

Reference(sheet,                    #giving range of the row and column
          min_row=2,
          max_row=sheet.max_row,
          min_col=4,
          max_col=4)

chart =BarChart()
chart.add_data(values)
chart.add_chart(chart,'e2')     #e2 is which cell chart shld be visible


---let us make geenric piece if code can be used no of times by defining in funciton

import openpyxl as xl
from openpyxl.chart import BarChart,Reference

def process_workbook(filename):
    wb = xl.load_workbook('transaction.xlsx')  # here we are loading the excel
    sheet = wb["Sheet1"]
    for row in sheet(2, sheet.max_row + 1):
         cell = sheet.cell(row, 3)
         corrected_Cell = cell.value * 0.9
         corrected_Cell_row = sheet.cell(row, 4)  # in 4th column values of the correct will be printed
         corrected_Cell_row.value = corrected_Cell

    values = Reference(sheet,  # giving range of the row and column
              min_row=2,
              max_row=sheet.max_row,
              min_col=4,
              max_col=4)

    chart = BarChart()
    chart.add_data(values)
    chart.add_chart(chart, 'e2')

    wb.save(filename)