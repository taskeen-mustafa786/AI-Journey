#Challenge 14

import pandas as pd

df = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed"],
    "Age":[22,24,21],
    "Salary":[50000,65000,45000]
})

print(df)

# First Row with iloc

print(df.iloc[0])

# Second row using loc
print(df.loc[1])

# Age Column of first row
print(df.loc[0,"Age"])

# Name and Salary of Sara only
print(df.loc[1,["Name","Salary"]])

# Rows where age is greater than 22
print(df.loc[(df["Age"]>22)])