import pandas as pd
# Read data from csv file into a datafarme.
df=pd.read_csv("sales.csv",encoding="latin1") # encoding="utf-8" - use one of them if there is error.
print(df)

# Read data from excel file into a datafarme.
df1=pd.read_excel("data.xlsx")
print(df1)

## Read data from json file into a datafarme.
df2=pd.read_json("path")
print(df2)

## if data is stored in cloud-us #gcsfs library.


