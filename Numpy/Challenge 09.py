# Challenge 09:

import numpy as np

A = np.array([
    [1,2,3],
    [4,5,6]
])

v1 = np.array([1,2,3])

v2 = np.array([4,5,6])

# Shape of A:
print(A.shape)

# Print A.T
print(A.T)

# Print the shape of A.T
transposed = A.T
print(transposed.shape)

# Find np.dot(v1,v2)
print(np.dot(v1,v2))

# By hand: without code
# np.dot(
#    np.array([1,1,1]),
#    np.array([2,3,4])
#) #Answer=> 9
# 
# difference B/W Vector and matrix: vector is 1D array wheras, matrix is 2D array.  