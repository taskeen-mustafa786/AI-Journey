# reshape()

## This is one of the most important NumPy operations for:

#* Machine Learning datasets
#* Deep Learning tensors
#* Computer Vision images
#* Data preprocessing

## Example
import numpy as np

arr = np.array([1,2,3,4,5,6])

print(arr) ## Shape = (6,)

## Convert to 2 Rows × 3 Columns
new_arr = arr.reshape(2,3)

print(new_arr) # shape = (2,3)

## Convert to 3 Rows × 2 Columns
new_arr = arr.reshape(3,2)

print(new_arr) # shape = (3,2)

## Rule :  Total elements must remain the same. 

## Possible combinations : 
# 2 × 3 = 6
# 3 × 2 = 6
# 1 × 6 = 6
# 6 × 1 = 6

## Not possible 4 x 2 = 8, then gives "ValueError"

