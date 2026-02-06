# Describe Method 

import pandas as pd
data={

"Name":['Ram','Krishna','Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,34,22,30,29,40,25,32],
"Salary":[50000,60000,45000,52000,49000,70000,48000,58000],
"Performance":[85,90,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
print("Sample Dataframe")
print(df)

print("Descriptive statistics")
print(df.describe())




'''   
A DataFrame is a fundamental 2-dimensional labeled data structure in data analysis (especially Python's pandas library, pandas) that organizes data into rows and named columns, similar to a spreadsheet or SQL table, allowing for efficient data manipulation, analysis, and storage of various data types. 
It's the most common pandas object, offering rich functionality for handling datasets.

'''