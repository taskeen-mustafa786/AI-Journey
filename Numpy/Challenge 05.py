# Practice Challenge 05 :

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# Part A : into shape (3,4)
p_a = arr.reshape(3,4)

# Part B : into shape 4,3
p_b = arr.reshape(4,3)

# Part C: print shape of p_a,p_b
print("Part A array shape := ",p_a.shape)
print("Part B array shape := ",p_b.shape)

# Part D answer by hand, arr.reshape(2,6)
## its shape will be (2, 6) and array will be:
#[
#   [ 1, 2, 3, 4, 5, 6],
#   [ 7, 8, 9,10,11,12]
#]

## Part E : Will this work : arr.reshape(5,3)
## Answer : No, because 5x3 = 15, that breaks rule that
## number of elements always remain same
## So, it will give ValueError