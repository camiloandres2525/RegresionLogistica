import numpy as np

# Creamos un arreglo de dos dimensiones
a = np.array([[1, 2] , [3, 4]])
# Imprimimos el arreglo
print(a)

# Imprimos la forma (shape) del arreglo
print(a.shape) # shape = este atributo devuelve una tupla con el tamaño del arreglo (array)
# En este caso el tamaño del arreglo (array) = (2,2)
# (2,2) = el tamaño del arreglo son dos filas, dos columnas

# Se pueden realizar operaciones aritmeticas entre arreglos
b = np.array([[5, 6] , [7,  8]])

# Suma
print(a + b)

# Multiplicacion
print(a * b)

# Multiplicacion de un escalar por un arreglo
print(2 * a) # Multiplicacion escalar = se refiere al producto de un numero real por una matriz

# Transposición de un arreglo
print(a.T) # Transposición = es una forma especial de redimensionar 

# Cálculo de la media de los elementos del arreglo
print(np.mean(a))



