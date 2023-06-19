import pandas as pd

# Carga de datos en archivo csv

titanic = pd.read_csv("titanic.csv")
# Se imprimen las primeras 5 filas del DataFrame
print(titanic.head())

# Seleccion solo las filas correspondientes a los sobrevivientes del titanic
sobrevivientes_titanic = titanic.loc[titanic["Survived"]]

# Calcular la suma de los sobrevivientes del titanic
total_sobrevivientes = sobrevivientes_titanic["Survived"].sum()
# Imprime el resultado 
print("El total de sobrevivientes de los datos recaudados son: ",total_sobrevivientes)