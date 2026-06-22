# Challenge 16:

import pandas as pd

students = pd.DataFrame({
    "Name":["Ali","Sara","Ahmed","Ayesha","Usman"],
    "Age":[22,24,21,25,23],
    "Marks":[90,85,95,88,80]
})

# Saving as students.csv

students.to_csv("students.csv",index=False)

# Reading back
st_df = pd.read_csv("students.csv")