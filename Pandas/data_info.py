# info of the datasets.summarize datasets.
# 
''''    
#problems
1.how much columns,rows?
2.which columns,rows?
3.missing data in which colums or rows?

# info() method gives:
1. number of rows & columns
2.columns name 
3.data types(int64 float64 object)
4.non null counts
5. memeory usages of the dataframe.

'''
import pandas as pd
df= pd.read_json("data.json")
print('Display the info of dataset')
print(df.info())