# Challenge 11:

import numpy as np

arr = np.array([5,10,15,20,25,30])

# Part A : Print values greater than 15. Expected:[20 25 30]
print(arr[arr>15])

# Part B : Print values less than or equal to 20. 
# _Expected:[5 10 15 20]
print(arr[arr<=20])

#Part C : Print values equal to 15. Expected:[15]
print(arr[arr==15])

#Part D : Print values between 10 and 25 inclusive. 
# _Expected: [10 15 20 25]
print(arr[(arr>=10) & (arr<=25)])

# Part E : Print values: < 10 OR > 25, Expected: [5 30]
print(arr[(arr<10) | (arr>25)])