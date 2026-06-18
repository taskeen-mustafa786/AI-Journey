# Fancy Indexing
## Get multiple specific elemnts from array 
# _by applying multiple indices at once

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[[0,2,4]])

## Another Example
arr = np.array([100,200,300,400,500])

print(arr[[1,3]])

## Fancy Indexing in 2D Arrays 
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# Get 0 and 2 indexed row
print([0,2])

# Axis Operations

# Sum of all elements
np.sum(arr) # 450

# Sum Row-Wise
np.sum(arr,axis=1) # [60 150 240]

# Sum Column-Wise
np.sum(arr, axis=0)