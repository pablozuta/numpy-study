import numpy as np 

# sample data
data = np.array([11, 22, 33, 44, 55, 66])
print("Original Array:", data)

# calculate mean and standard deviation
mean = np.mean(data)
standard_deviation = np.std(data)

# print the result
print("Mean: ", mean)
print("Standard Deviation: ", standard_deviation)