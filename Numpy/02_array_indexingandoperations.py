# Array Indexing
import numpy as np

## Indexing is extremely important because in ML datasets 
# you'll constantly access rows, columns, features, and labels.

## 1D Array Indexing
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])

### Access last element
print(arr[-1])

### Negative indexing starts from the end.

## 2D Array indexing 
arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

### Access 5
print(arr[1,1])

### Access 9
print(arr[2,2])

### Access 7
print(arr[2,0])