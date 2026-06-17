# Broadcasting and Vectorization

## if we add arr+5 it is not possible in simple python arrays, 
## and will produce error
## So, in numpy when you add arr+5, 
## it broadcasts value 5 and create new array that 
# matches the shape of array to be performed with
## For Example arr = np.array([1,2,3])
## then arr = arr+5 will be [1,2,3]+[5,5,5]
## So, operation of converting a number into suitable array
#  for performing the specified operation 
# is called broadcasting

## Performing operations between two equal shape arrays 
# is called Vectorization 

## Some Examples
import numpy as np

arr = np.array([10,20,30])

print(arr + 2) # +2 to each element
print(arr - 2) # subtract 2 from each element
print(arr * 2) # multiply 2 to each element
print(arr / 2) # Divide each element by 2
print(arr ** 2) # Square each element


numbers = [1,2,3,4]

result = []

for n in numbers:
    result.append(n*2)

print(result)

#  Advantages 
# faster, less code and used everywhere in AI.