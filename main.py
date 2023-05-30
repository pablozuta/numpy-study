import numpy as np #aca importamos el modulo externo para poder usar numpy


a = np.zeros(30) # array de ceros con 30 elementos
print(a)
print(f'{type(a)}tipo de dato del objeto')
print(f'{type(a[0])}tipo de dato de cada elemento')


ones = np.ones(66) ## array de unos con 66 elementos
print(ones)
print(f"{type(ones)} tipo de dato del objeto")# ndarray
print(f"{type(ones[0])}tipo de dato de cada elemento")# float64

# One dimensional ndarray
array_one = np.array([22, 33, 44, 55, 66])
print(array_one)
print(type(array_one))
print(type(array_one[0])) # int32

# Two dimensional ndarray
array2D = np.array([[2, 3, 4], [4, 6, 8]])
print(array2D)
# acceder a un elemento usando index (2 maneras)
print(array2D[1][1])
print(array2D[1, 1])
print(f"{type(array2D)}tipo de dato del objeto")
print(f"{type(array2D[0][0])}tipo de dato de cada elemento")


