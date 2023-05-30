import numpy as np 

# create a 1D array
array1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# reshape the array to a 2x5 matrix
array2D = np.reshape(array1D, (2, 5))

# print the array
print(array2D)