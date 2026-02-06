# concatenation of dataframe.

"""   
combining dataframe either vertically or horizontally
syntax:
pd.concate([df1,df2],axis=0,ignore_index=True)
axis=0-rowise combine, axis-1= column wise.
ignore_Index=True- reset index of combined dataframe.

"""

import pandas as pd
df_region1=pd.DataFrame(
    {
'Customer ID':[1,2],
'Name':['Gopal','Raju']

    }
)

df_region2=pd.DataFrame(
    {
'Customer ID':[3,4],
'Name':['Hari','Baburam']

    }
)

# concatenanting vertically.
df_concat=pd.concat([df_region1,df_region2],axis=0,ignore_index=True)
print(df_concat)

# concatenanting Horizontally.
df_concat=pd.concat([df_region1,df_region2],axis=1,ignore_index=True)
print(df_concat)