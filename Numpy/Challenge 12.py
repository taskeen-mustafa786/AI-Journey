# Challenge 12:

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

arr2 = np.array([10,20,30,40,50])

# A:
print(arr2[0,2,4])

# B: Printing rows
print(arr[0,2])

# C: sum of arr, without runing code:=> 450

# D: sum, np.sum(arr, axis=0), without code: => [120 150 180]


# E: sum, np.sum(arr, axis=1), without code: => [60 150 240]