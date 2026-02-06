# Adding column:

import pandas as pd
data={

"Name":['Ram','Krishna','Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,34,22,30,29,40,25,32],
"Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
"Performance":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
# adding column via assignment- squire brackets df ["Column_Name"]=Some_Data

print(df)

df["Bonus"]=df["Salary"]*0.1 # creating a column for 10% Bonus.
print(df)

# Using insert() methods:-most recommended.
# df.insert(loc,"Column_Name",Some_Date)

df.insert(0,"Employee Id",[10,20,30,40,50,60,70,80])

print(df) 