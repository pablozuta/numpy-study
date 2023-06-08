import numpy as np 

height = np.array([1.65, 1.72, 1.80, 1.68, 1.75]) # height in meters
weight = np.array([68, 72, 80, 65, 70])

bmi = weight / height ** 2

# show the results
print("BMI Values:", bmi)