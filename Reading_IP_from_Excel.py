#importin required Libraries
import xlrd
import openpyxl
import pandas as pd

# Creating an Empy Dictionary
d={}

#importing data of excel file and storing it as a list
df=pd.read_excel("C:\\Users\\Ifra\\Desktop\\xyz.xlsx","Sheet1")
IP_add=df["IP Addresses"].values.tolist()
name=df["Names"].values.tolist()

#printing created list
print(IP_add)
print(name)

#Zipping two lists to make one file
zipobj=zip(IP_add,name)

#creating a dictionary from zipped file
d=dict(zipobj)

#printing dictionary
print(d)
