import numpy as np #aca importamos el modulo externo para poder usar numpy
import matplotlib.pyplot as plt 

a = np.zeros(30) # array de ceros con 30 elementos
print(a)
print(f'{type(a)}tipo de dato del objeto')
print(f'{type(a[0])}tipo de dato de cada elemento')


ones = np.ones(66) ## array de unos con 66 elementos
print(ones)
print(f"{type(ones)} tipo de dato del objeto")# ndarray
print(f"{type(ones[0])}tipo de dato de cada elemento")# float64

names = np.array(["John", "ALice", "Pharoah", "Albert"]) # array de strings
print(names)

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

array_random1 = np.random.random(10) # numeros entre 0 y 1
array_random2 = np.random.randn(10) # normal distribution (entre -1 y 1)
print(array_random1)
print(array_random2)

array_linear = np.linspace(0, 10, 20) # crea 20 numeros desde 0 a 10 usando incremento linear entre cada numero
print(array_linear)

array_arange = np.arange(0, 10, 0.02) # crea numeros de 0 a 10 en incrementos de 0.02 
print(array_arange)

## ARRAY OPERATIONS
print("Suma: ", array_one + 10) 
print("Resta: ", array_one - 10) 
print("Multiplicacion: ", array_one * 10) 
print("Division: ", array_one / 10) 
print("Potencia: ", array_one ** 2) 
print("Boolean: ", array_one > 40)


## INDEXING
print(array_one[0]) # index 0
print(array_one[0]) # index 0
print(array_one[1:]) # desde index 1 al final
print(array_one[1:-1]) # desde index 1 al penultimo elemento
print(array_one[1:-2]) # desde index 1 al antepenultimo elemento
print(array_one[array_one < 45]) # usando una expresion booleana como index
print(array_one[array_one > 43]) # usando una expresion booleana como index
print(array_one[array_one == 44]) # usando una expresion booleana como index



## PLOTING
x = np.linspace(0, 1, 100)
y = x ** 2

plt.plot(x, y) # hace un plot linear desde el valor de x hasta el valor de x * x(y)
plt.show()

plt.hist(array_random1) # hace un plot en barras
plt.show()