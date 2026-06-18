# Linear Algebra Basics

## Why Linear Algebra Matters

### Almost every ML/DL operation is based on:

### Vectors
### Matrices
### atrix Multiplication

## Neural networks are essentially huge matrix operations.

### Example:
### Input Features
###       ↓
### Weights Matrix
###       ↓
### Matrix Multiplication
###       ↓
### Predictions

import numpy as np

## Vector: 1D Array
vector = np.array([1, 2, 3]) # shape => (1,)

## Matrix: 2D Array
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
]) # shape: (2,3) 
 
## Transpose: Rows become columns
print(matrix.T) # output shape: (3,2)

### Why Useful? => In ML and DL, transposes are constantly 
### _used when multiplying matrices and preparing data.

## Dot Product
a = np.array([1,2,3])

b = np.array([4,5,6])

print(np.dot(a,b))

###  ML Interpretation: 
### _suppose:
### _Features = [Age, Salary, Experience]
### _Weights  = [0.2, 0.5, 0.3]
### prediction: dot(features,weights)

