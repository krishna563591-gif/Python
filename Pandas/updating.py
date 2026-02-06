# Updating values:
# syntax:
# .loc[]
# df.loc[row_index,"Colum_Name"]=new_value



import pandas as pd
data={

"Name":['Ram','Krishna','Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,34,22,30,29,40,25,32],
"Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
"Performance":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
df.loc[0,"Salary"]=55000 # precise location.
print(df) # salary of ram becomes-55000.


# Increasing salary by 5%.
df['Salary']=df['Salary']*1.05
print(df)