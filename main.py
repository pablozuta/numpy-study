import numpy as np #aca importamos el modulo externo para poder usar numpy

def erase():  #definimos una funcion de salto de linea
    print('')

erase()
erase()
erase()

#aca creamos un numpy array de ceros, que tiene valores individuales de tipo float64
print('aca creamos un array de ceros con np.zeros')
a = np.zeros(30)
print(a)
print(f'{type(a)} es el tipo del objeto creado')
print(f'{type(a[0])} es el tipo de dato de cada elemento del array')
erase()

#aca creamos un numpy array de unos, que tiene valores individuales de tipo float64
print('aca creamos un array de unos con np.ones')
ones = np.ones(66)
print(ones)
print(type(ones))
print(type(ones[0]))
erase()
erase()
erase()

