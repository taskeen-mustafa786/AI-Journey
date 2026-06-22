#CSV = Comma Seperated Values
# EDA : Exploratory Data Analysis


import pandas as pd

df = pd.read_csv("/workspaces/AI-Journey/Pandas/employees.csv")

print(df)

# df.head() => For viewing first rows
print(df.head(3))

# df.tail() => for viewing last rows
print(df.tail(3))

# DF Shape
print(df.shape)

# Column names
print(df.columns)

# Info about df : Shows: Rows, Columns, Data Types, Missing Values
print(df.info())

# df Stastistics: Output contains:count, mean, std, min, 25%, 50%, 75%, and max for numerical columns.
print(df.describe())

# Why These Commands Matter?

## Whenever a Data Analyst gets a dataset, they usually this before anything else. This is called exploratory data analyis


# Creating your own CSV
import pandas as pd

df = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed"],
    "Age":[22,24,21],
    "Salary":[50000,65000,45000]
})

df.to_csv("employees2.csv", index=False)

# This creates employees2.csv file

