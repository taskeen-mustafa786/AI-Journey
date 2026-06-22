# Challenge 15.2
import pandas as pd

df = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed","Ayesha"],
    "Age":[22,24,21,25],
    "Salary":[50000,65000,45000,70000]
})

# First two rows using df.head()
print(df.head(2))

# Last two rows using df.tail()
print(df.tail(2))

# Df.info() => provides info about dataframe
print(df.info())

# Employees where Age>21 and Salary > 50000
print(df[(df["Age"]>21) & (df["Salary"]>50000)]["Name"])

# Employees where Age<22 or Salary > 60000
print(df[(df["Age"]<22) | (df["Salary"]>60000)]["Name"])
