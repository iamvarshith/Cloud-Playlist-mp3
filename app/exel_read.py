# import module
import openpyxl

# load excel with its path
wrkbk = openpyxl.load_workbook("C:\\Users\\varsh\\Downloads\\music_xl.xlsx")

sh = wrkbk.active

# iterate through excel and display data
for i in range(2, 3):
    print("\n")
    print("Row ", i, " data :")

    for j in range(1, 5):
        cell_obj = sh.cell(row=i, column=j)
        print(cell_obj.value, end=" ")
