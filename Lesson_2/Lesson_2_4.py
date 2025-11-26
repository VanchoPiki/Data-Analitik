import numpy as np

arr = np.arange(1, 13)
print(arr)

#[ 1  2  3  4  5  6  7  8  9 10 11 12]

reshape = arr.reshape((3, 4))
print(reshape)

#[[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]