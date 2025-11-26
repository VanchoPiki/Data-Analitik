import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

hstack = np.hstack((arr1, arr2))
print(hstack)

#[1 2 3 4 5 6]

vstack = np.vstack((arr1, arr2))
print(vstack)

#[[1 2 3]
#[4 5 6]]

matrix = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8]
])

hsplit = np.hsplit(matrix, 2)
print(hsplit)

#[array([[1, 2],    array([[3, 4],
#       [5, 6]]),          [7, 8]])]
#

vsplit = np.vsplit(matrix, 2)
print(vsplit)

#[array([[1, 2, 3, 4]]), array([[5, 6, 7, 8]])]