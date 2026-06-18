# Advanced Stastistics

import numpy as np

arr = np.array([10,20,30,40,50])


## Median = middle value after sorting 
print(np.median(arr))

### Why median? => Because, mean can be misleading 
### _in case of higher outliers such as, 
### _Mean of [20,25,30,35,1000] is 222 and median is 30.
### _Due to higher outliers mean become so large 
### _that is very far from center
### _That's why, analysts also check median with mean.

## Variance: Measures how spreadout data is
print(np.var(arr))

### Low Variance: Values are close together
### High Variance: Values are spreadout