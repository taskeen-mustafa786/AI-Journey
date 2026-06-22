#Challenge 15


import pandas as pd

df = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed","Ayesha"],
    "Age":[22,24,21,25],
    "Salary":[50000,65000,45000,70000]
})

# Avg age
print(df["Age"].mean())

# Max Salary
print(df["Salary"].max())

# Min Salary
print(df["Salary"].min())

# Total salary of all employees
print(df["Salary"].sum())

# Df.describe()
print(df.describe())

# without code: df["Age"].max() =>25

# Employees with Salary greater than 50000

print(df.loc[df["Salary"]>50000]["Name"])