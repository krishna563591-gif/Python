# Numerical Summaries Of the data.
'''
df['column Nme'].mean()
df['column Nme'].sum()
df['column Nme'].min()
df['column Nme'].max()

'''
import pandas as pd
data={
"Name":['Arun','Varun','Karun'],
"Age":[28,34,22],
"Salary":[1000,2000,3000]

}
df=pd.DataFrame(data)
avg_salary= df["Salary"].mean()
print(avg_salary)
