# How can we view rows using pandas.
# Two Methods: to check status of data.
# Head (n) -show n rows otherwise first 5 rows.
#  tail(n)-show last n rows otherwise last 5 rows.

import pandas as pd
df= pd.read_json("data.json")
print('Display 10 rows of frist')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))



# ==================================================