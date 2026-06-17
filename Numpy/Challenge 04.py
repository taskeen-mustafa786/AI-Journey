# Practice Challenge 04 :
import numpy as np
## PART A: ZEROS : [0. 0. 0. 0. 0.]
print(np.zeros(5))

## PART B: Ones: [
 ##                 [1. 1.]
 ##                 [1. 1.]
##               ]

print(np.ones((2,2)))

## PART C: FULL : [
 ##                 [9 9 9]
 ##                 [9 9 9]
##                ]

print(np.full((2,3),9))

## Part D: Arange : [5 6 7 8 9 10]
print(np.arange(5,11))

## Part E : Arange : [0 5 10 15 20 25]
print(np.arange(0,30,5))

## Part F: Linspace : equally spaced values between 0 and 50
print(np.linspace(0,50,6))