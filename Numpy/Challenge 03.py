# Practice Chaalenge 03

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

## Part A
### First row
print(arr[0])

### Last Row
print(arr[-1])

### First Column 
print(arr[:,0])

### Last Column
print(arr[:,-1])

## Part B

## Print [20 30]
print(arr[0,1:])

## Part C : print [40 50]
print(arr[1,:2])

## Part D
## Print 
# [
# [10 20]
# [40 50]
# ]

print(arr[0:2,0:2])

arr = np.array([10 20 30 40 50])

# Reversed
print("Reversed := ", arr[::-1])