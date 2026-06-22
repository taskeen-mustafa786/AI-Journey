# Challenge 13:
import pandas as pd

## Create series => [10,20,30,40,50] and store it in numbers.
numbers = pd.Series([10,20,30,40,50])
print(numbers)

## Create a Series:
## * Ali = 90
## * Sara = 85
## * Ahmed = 95

## _using custom index and Print it.

records = pd.Series([90, 85, 95], index=["Ali","Sara","Ahmed"])
print(records)

## Ahmed's marks
print(records["Ahmed"])

df = pd.DataFrame({
    "Name":["Ali", "Sara", "Ahmed"],
    "Age":[22,24,21],
    "Salary":[50000, 65000, 45000]
})

#Shape 
print(df.shape)

#Columns
print(df.columns)

#Name only
print(df["Name"])

#Name and Salary
print(df[["Name","Salary"]])



