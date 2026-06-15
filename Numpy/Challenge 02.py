#Challenge 02

## Print:

#10
#50
#90
#80
#40

#Then answer:

# What does arr[0,2] return?
# What does arr[2,0] return?
# What does arr[-1,-1] return?

import numpy as np 
arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

# 10
print(arr[0,0])

#50
print(arr[1,1])

#90
print(arr[2,2])

#80
print(arr[2,1])

#40
print(arr[1,0])

# What does arr[0,2] return?
# 30

# What does arr[2,0] return?
# 70

# What does arr[-1,-1] return?
# 90