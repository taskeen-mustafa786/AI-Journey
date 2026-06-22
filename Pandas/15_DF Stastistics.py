import pandas as pd

df = pd.DataFrame({
    "Age":[22,24,21],
    "Salary":[50000,65000,45000]
})

# Mean
print(df["Age"].mean())

# Minimum
print(df["Salary"].min())

# Sum
print(df["Salary"].sum())

# Maximum
print(df["Salary"].max())

# Describe => Shows stastistics of complete dataframe
print(df.describe())