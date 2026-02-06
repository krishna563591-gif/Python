# Saving data as csv,excel or json file after creating.
import pandas as pd
data={
"Name":['Ram','shyam','krishna'],
"Age":[10,20,30,],
"City":['Nagpur','Simla','Mumbai']

}

df=pd.DataFrame(data)
print(df)
#df.to_csv("output.csv",index=False) # Saving to csv file.
df.to_excel("output.xlsx",index=False) # saving to excel
df.to_json("output.json",index=False) # saving to json