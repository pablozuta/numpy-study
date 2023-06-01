import numpy as np 

# create 2 arrays
array1 = np.array([11, 22, 33, 44])
array2 = np.array([55, 66, 77, 88])

# Perform element-wise addition, subtraction, multiplication, and division
addition = np.add(array1, array2)
substraction = np.subtract(array1, array2)
multiplication = np.multiply(array1, array2)
division = np.divide(array1, array2)

# mostrar los resultados
print("Addition: ",addition)
print("Substraction: ",substraction)
print("Multiplication: ",multiplication)
print("Division: ", division)