import numpy as numpy

# Array Creation Functions

## Instead of manually typing: np.array([1,2,3,4,5])

## NumPy provides functions to automatically generate arrays.

## 1. zeros() : Creates an array filled with zeros.

### 1D
arr = np.zeros(5)
print(arr)

### NumPy creates float values by default.

### 2D
arr = np.zeros((3,4))

print(arr)

## 2. Ones
arr = np.ones((2,3))

print(arr)

## 3. full() : Fill entire array with a specific value.
arr = np.full((3,3), 7)

print(arr)

## Why Useful?

## Imagine:

#* Initializing neural network values
#* Creating masks
#* Creating test datasets

## 4. arange()

## Works like Python's range() but returns a NumPy array.
arr = np.arange(5)

print(arr) # output: [0 1 2 3 4]

arr = np.arange(2,10) 

print(arr) # output : [2 3 4 5 6 7 8 9]

arr = np.arange(0,20,2)

print(arr) # [ 0  2  4  6  8 10 12 14 16 18]

## np.arange(start, stop, step)

## 5. linspace()

### Very important in:

#* Machine Learning
#* Deep Learning
#* Graph plotting
#* Data Science

### Creates equally spaced values.

arr = np.linspace(0,10,5)

print(arr) # [ 0.   2.5  5.   7.5 10. ]