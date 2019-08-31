import pandas as pd

d={}
file=pd.read_excel("C:\\Users\\Ifra\\Desktop\\xyz.xlsx","Sheet1")
IP_add=file["IP Addresses"].values.tolist()
name=file["Names"].values.tolist()

print(IP_add)
print(name)

zipobj=zip(IP_add,name)

d=dict(zipobj)

print(d)