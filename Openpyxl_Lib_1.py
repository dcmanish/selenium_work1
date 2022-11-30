import openpyxl
workbook=openpyxl.load_workbook("C:\\Users\\admin\\Desktop\\jupyter\\Book1.xlsx")
sheet=workbook['Sheet1']
a=sheet['A1'].value
print(a)

