#Numpy

##Arrays

import numpy as np

print("Numpy arrays practice")

### Sample arrays
a1 = np.array([1,2,3])
print("Simple Array",a1)

### 2D Arrays
a2 = np.array([[1,2,3],[1,2,3]])
print("2D Array",a2)

### 3D Arrays
a3 = np.array([
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [7,8,9],
        [10,11,12]
    ]
])

print("3D Arrays",a3)


## Array operations

### Array Dimensions
print("Array dimension, a2 = ",a2.ndim)

### Array Size
print("Number of elements in a3 = ",a3.size)

### Array Shape
print("Shape of A3 = ",a3.shape)

### Array Type 
print("Type of an array, a3 == ",a3.dtype)