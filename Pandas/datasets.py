# Datasets: how big is your dataset,what are the name of columns.
# we use
#  shape-to know how big is dataset(rows,columns).
# & columns-these are attibute(Gives name of columns)
import pandas as pd
data={

"Name":['Ram','Krishna','Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,34,22,30,29,40,25,32],
"Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
"Performance":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
print(df)

print(f'shape:{df.shape}')
print(f'Columns Names:{df.columns}')