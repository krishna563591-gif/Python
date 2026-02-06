# Sorting datas:

# sorting data in one column: sort_values()
# syntax: df.sort_values(by="Column Name",True/False) (ascending-true,descensing- false)
import pandas as pd
data={
"Name":['Arun','Varun','Karun'],
"Age":[28,34,22],
"Salary":[1000,2000,3000]

}

df=pd.DataFrame(data)
# Sorting Age in a Ascending order.
df.sort_values(by="Age",ascending=True,inplace=True)
print(df)

# sorting Age in Descending Order.
df.sort_values(by="Age",ascending=False,inplace=True)
print(df)


# Multiple Columns Sorting.
df.sort_values(by=["Age","Salary"],ascending=[True,False],inplace=True) # In here- first column is true-asced & second one false-descending order.
print(df)