# Challenge 08:

import numpy as np

arr = np.array([5,10,15,20,25])

## Median
print(np.median(arr))

## Variance
print(np.var(arr))

## Standard Deviation
print(np.std(arr))

## Without code: np.median([1,3,5,7,9]) => 5

## Which statistic is generally less affected by extreme outliers?
## _Mean or
## _Median
## _and why?
## Answer: Median, because it always chooses middle value after so no matter how big outlier is, can not affect results 
## _but too many outliers at one side still can affect results.