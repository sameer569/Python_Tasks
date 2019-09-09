import os,shutil,glob
import openpyxl
(os.chdir("C:\\Users\\Ifra Fatimah\\Desktop\\New folder (3)\\file_1\\file_2\\file_3"))
path="C:\\Users\\Ifra Fatimah\\Desktop\\New folder (3)\\file_1\\file_2\\file_3"
s=glob.glob("*.txt")
print(s)
wbpath="C:\\Users\\Ifra Fatimah\\Desktop\\text_files_only.xlsx"
workbook=openpyxl.load_workbook(wbpath)
sheet=workbook.active
r=1
c=1
for i in s:
    sheet.cell(row=r,column=c).value=i
    r +=1
workbook.save(wbpath)