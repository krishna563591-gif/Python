# Removing Coumns:to remeove any column & rows
# syntax:
# df.drop(columns=["ColumnName"],inplace=True) # inplace True= means modify the original dataframe directly.

import pandas as pd
data={

"Name":['Ram','Krishna','Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,34,22,30,29,40,25,32],
"Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
"Performance":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
# removing sigle column.
df.drop(columns=["Performance"],inplace=True)
print(df)
'''
# removing multiple columns.
print("Modified Dataset")
df.drop(columns=["Performance","Age"],inplace=True)
print(df)
'''