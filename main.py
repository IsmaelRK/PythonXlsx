import openpyxl

workbook = openpyxl.load_workbook('alunos.xlsx')
sheet = workbook.active


fullTable = []
fullLine = []
for row in sheet.iter_rows():
    for cell in row:
        fullLine.append(cell.value)
    fullTable.append(fullLine)
    fullLine = []

print(fullTable)
