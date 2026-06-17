# NumPy Slicing

## Indexing gets one value.

## Slicing gets multiple values.

## This is one of the most important concepts in:

#* NumPy
#* Pandas
#* Machine Learning
#* Deep Learning
#* Computer Vision


import numpy as np 

## 1D Array Slicing

arr = np.array([1,2,3,4,5,6,7,8,9])

### First Three elements
print("First three elements of an array := ",arr[0:3])

### Rule [start:end] 
### Start is included
### End is discluded

#### from begining to a point
print(arr[:4])

#### from a point to an end
print(arr[4:])

#### Entire array
print(arr[:])

### Step Size
### Rule [start:end:step]

#### Every Second Element
print("Every second element : = ",arr[::2])

### Reverse Array
print("Reversed array := ",arr[::-1])

## 2D Array Slicing

arr = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

### First Row 
print("First row of an array := ",arr[0])

### Second Row 
print("Second row of an array := ",arr[1])

### First Column 
print("First column of an array := ",arr[:,0])


### Second Column
print("Second column of an array := ",arr[:,1])

### Third Column
print("Third column of an array := ",arr[:,2])

### First Two rows
print("Frst two rows := ",arr[:2])

### Last Two rows
print("Frst two rows := ",arr[1:])

### First two columns
print("First two columns := ",arr[:,0:2])
