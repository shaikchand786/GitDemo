import openpyxl
#Dict = {}
book = openpyxl.load_workbook("C:\\Users\\HP\\Documents\\DemoXL.xlsx")
sheet = book.active
cell = sheet.cell(row=2, column=2)
#print(cell.value)
# sheet.cell(row=6, column=1).value = "Aayesha"
# print(sheet.cell(row=6, column=1).value)
# print(sheet["B3"].value)
# print(sheet.max_row)
# print(sheet.max_column)

for i in range(1, sheet.max_row+1):
#    if sheet.cell(row=i, column=4).value == "Male":
    for j in range(1, sheet.max_column+1):
        print(sheet.cell(row=i, column=j).value)
#                Dict[sheet.cell(row=1, column=j).value] = sheet.cell(row=i, column=j).value

#print(Dict)