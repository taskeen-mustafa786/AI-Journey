# Introduction to Pandas
## Numpy is best for numbers, but, 
## -in Numpy we don't know which column is age, which is salary
## _having no labels
## _Hard to work without labels
## _Pandas solves these problems by adding labels for columns.

## Two main pandas objects 

## 1. Series : A single column

import pandas as pd

ages = pd.Series([22,24,21])

print(ages)

## 2. Dataframe : A complete table

df = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed"],
    "Age":[22,24,21]
})

print(df)

## Dataframe is collection of series

# Series 
## Creation:
import pandas as pd

s = pd.Series([10,20,30,40])

print(s)

## Series with custom index:

s = pd.Series(
    [90,85,95],
    index=["Ali","Sara","Ahmed"]
)

print(s)

## Accessing values :
print(s["Ali"])

# Dataframe
## Creation
df = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed"],
    "Age":[22,24,21],
    "Salary":[50000,65000,45000]
})

## Viewing dataframe :
print(df)

## Dataframe shape
print(df.shape)

## Dataframe Columns
print(df.columns)

## Dataframe information
print(df.info()) # One of the most used commands in data analysis

## Selecting one column
print(df["Name"])

## Selecting multiple columns
print(df["Name","Salary"])