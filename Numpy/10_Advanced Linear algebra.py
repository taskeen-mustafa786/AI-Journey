# Matrix Multiplication

## This is the most important linear algebra operation for ML and DL.

import numpy as np

## Element-wise Multiplication
A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

print(A * B)

## This is not matrix multiplication.

# Actual Matrix Multiplication

print(A @ B)

#or

np.matmul(A,B)