import numpy as np

A = np.array([
    [1,2],
    [3,4]
])

B = np.array([
    [5,6],
    [7,8]
])

# Part A: Perform element-wise multiplication.
print(A*B)

# Part B : Perform matrix multiplication.
print(A@B)

# Part C : Without running code, calculate: A@B
# row_a_1 x col_b_1 = 1x5 + 2x7 =   19
# row_a_1 x col_b_2 = 1x6 + 2x8 =   22
# row_a_2 x col_b_1 = 3x5 + 4x7 =   43
# row_a_2 x col_b_2 = 3x6 + 4x8 =   50
# result : 
# [
#    19 22
#    43 50
#]

# Part D: Difference between A*B and A@B 
# _A*B => element wise -> each element of first matrix is 
# _multiplied with the lement of second matrix at the same index
# _A@B: Each row of first matrix element-wise multiplied with 
# _each column of second matrix.