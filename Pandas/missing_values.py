# Missing Values.
#1.Nan(Not a Number)
#2.None (for object data types)

'''    
# Before handling missing data - we need to identify where the datas are mising.
# Method:
isnull()- returns boolean(true or false)
True=NaN is missing
False=value is present
'''

# Example:1
'''
import pandas as pd
data={

"Name":['Ram',None,'Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,None,22,30,29,40,25,32],
"Salary":[50000,None,45000,52000,49000,70000,48000,58000],
"Performance":[85,None,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull())

'''

# To know numbers of missing values.
# use-sum()

# print(df.isnull().sum())

# Handling Missing Datas:
#1.if the datas are not important-remove the row or columns if that does not affect your data.
'''
import pandas as pd
data={

"Name":['Ram',None,'Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,None,22,30,29,40,25,32],
"Salary":[50000,None,45000,52000,49000,70000,48000,58000],
"Performance":[85,None,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
df.dropna(inplace=True)
print(df)
'''

#2. Fill the values :
# fillna(value,inplace=True)

import pandas as pd
data={

"Name":['Ram',None,'Sita','Hari','Aditi','Raj','Simran','Asim'],
"Age":[28,None,22,30,29,40,25,32],
"Salary":[50000,None,45000,52000,49000,70000,48000,58000],
"Performance":[85,None,78,92,88,95,80,89]
}
df=pd.DataFrame(data)
'''
df.loc[1, "Name"] = "Krishna"
df.fillna(0,inplace=True) # filling default value-0 at misisng place. we can fill calculate value too e.g. mean.
print(df)

'''
#  Filling Calculated Value:
# For Age:
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)

# easy methods:
df.fillna({
    'Name': 'Krishna',
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].mean(),
    'Performance': df['Performance'].mean()
}, inplace=True)
print(df)




# interpolation- estimated value.