# Grouping of datas:
# syntax:
# df.groupby("Column_Name")- it creates a group based on the unique values in Age column.
# #["Salary"].sum()- aggregation value.


import pandas as pd
data= {
"Name":['Arun','Varun','Karun','Narun','Marun'],
"Age":[20,44,55,60,70],
"Salary":[50000,40000,30000,48000,70000],

}

df=pd.DataFrame(data)
grouped=df.groupby('Age')["Salary"].sum()
print(grouped)

# Grouping Multiple Columns.
grouped1=df.groupby(["Age","Name"]) ["Salary"].sum()
print(grouped1)

# Aggregation Operations:
#sum()
#mean()
#count()
#min()
#max()
#std()
