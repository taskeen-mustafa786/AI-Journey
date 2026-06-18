# Boolean Masking

## This is one of the most important NumPy topics for 
# _Data Cleaning, Pandas, Data Analysis, Machine Learning

# What is Boolean Masking?

# Suppose:
import numpy as np

arr = np.array([10,20,30,40,50])

## Find values greater than 25 :
print(arr > 25) #Output: [False False True True True]

#=> This Boolean Masking

## More examples:
print(arr==20) 
print(arr>=25)
print(arr<25)
print(arr<=20)
print(arr!=20)

# Multiple conditions
print((arr>=20) & (arr<=40)) # and
print((arr<25) | (arr>45)) # or

# Returning values meeting conditions
print(arr[arr > 15]) #Output : [15 20 25]
# All types of conditions that can applied can be applied above
#  _can be applied here too.