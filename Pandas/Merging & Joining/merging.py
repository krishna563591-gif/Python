# Merging:
# syntax: pd.merge(df1,df2, on="column_Name",how="type of join") 
import pandas as pd

#customer datafarme:
df_customers=pd.DataFrame({
    'Customer Id':[1,2,3],
    'Name':['Ramesh','Sita','Rita']
})

# Order Dataframe:
df_Order=pd.DataFrame({
    'Customer Id':[1,2,3,4],
    'OrderAmount':[200,450,350]
})

# Merge
'''
df_merged=pd.merge(df_customers,df_Order, on="Customer Id",how="inner" )
print("Inner Join")
print(df_merged)
'''
df_merged=pd.merge(df_customers,df_Order, on="Customer Id",how="outer" )
print("Outer join")
print(df_merged)

df_merged=pd.merge(df_customers,df_Order, on="Customer Id",how="right" )
print("right join")
print(df_merged)
# left join
df_merged=pd.merge(df_customers,df_Order, on="Customer Id",how="left" )
print("left join")
print(df_merged)
# cross join
df_merged=pd.merge(df_customers,df_Order, on="Customer Id",how="cross" )
print("Outer join")
print(df_merged)

''''     
Quick meaning refresher:

outer → all customers + all orders (NaN where missing)

right → all orders, matching customers if available

left → all customers, matching orders if available

'''