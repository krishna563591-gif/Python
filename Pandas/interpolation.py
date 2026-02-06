
# Interpolation:  filling an estimated values.
#1.Preserve data integrity.
#2.Smooth trends
#3.Avoid dataloss.

# methods:
#1.linear,polynominal,time-  know at least 7/8 more methods.

import pandas as pd
data={

"Name":['Ram',None,'Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,None,22,30,29,40,25,32],
"Salary":[50000,None,45000,52000,49000,70000,48000,58000],
"Performance":[85,None,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
print(df)

df.interpolate(method='linear',axis=0,inplace=True) #  axis 0-rows.axis 1-column.

