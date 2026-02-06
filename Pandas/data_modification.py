# Data Modification:
#1. selecting specific column.
#  column= df["Column Name"]- MULTIPLE COLUMNS- subset=df["column1","column2"......""]

#2. filter rows: boolean indexing.
# based on a single condition;
#filtered_rows=df[df["salary"]>50000]

# Combine multiple conditions;

#filtered_rows= df[(df["salary"]>50000) & (df["column2"]<80000)]
# ====================================

import pandas as pd
data={

"Name":['Ram','Krishna','Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,34,22,30,29,40,25,32],
"Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
"Performance":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
# display the dataframe.
print("Sample Dataframe")
print(df)

# selecting single column
print(df["Name"])

# Selecting Multiple Columns
subset=df[["Name","Salary"]]
print(subset)



# Filtering based on single condition.
high_salary=df[df['Salary']>50000]
print(high_salary)

# Filtering based on multiple conditions.

high_salary1= df[(df["Salary"]>50000) & (df["Age"]>30)]
print(high_salary1)

# Filtering based OR conditions.
filtered_or= df[(df["Age"]>35)|(df["Performance"]>90)] # will work even if its one condition is true.
print(filtered_or)

