# Pandas is a python library for designed for data manipulation & data analysis.

# Data Manipulations & Analysis:
'''   
Data Manipulation-Changing, cleaning, and organizing raw data so it becomes usable.

What we do:
Add / remove columns
Filter rows
Fix missing values
Change data types

Example (Pandas):

import pandas as pd

df = pd.DataFrame({
    "name": ["Ram", "Sita", "Hari"],
    "age": [20, None, 22]
})

df["age"] = df["age"].fillna(21)   # fixing missing data
print(df)


➡️ Here, we manipulated data by filling missing values.



Data Analysis-Studying data to find patterns, trends, and insights.

What we do:
Calculate averages
Find max/min
Group data
Draw conclusions


Example (Pandas):

print(df["age"].mean())   # average age


➡️ Here, we analyzed data to get information.

# One-line difference (easy to remember)

Manipulation → prepare & clean data

Analysis → understand & extract insights






'''