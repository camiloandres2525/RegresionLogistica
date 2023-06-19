import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import matplotlib.pyplot as plt


# Cargando archivo
archivo = pd.read_csv("diabetes.csv")
print(archivo.head())

# Estimando el modelo de regresion logistica
X = archivo[["BMI"]]
Y = archivo[["Outcome"]]

# Dividir la data en train(70%) y testing(30%)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.3, random_state=0)

# Instanciar el modelo 
regresion_logistica = LogisticRegression()

# Ajustar el modelo usando el training
regresion_logistica.fit(X_train, Y_train)

# Usar el modelo para hacer predicciones de testing
Y_pred = regresion_logistica.predict(X_test)
print(Y_pred)

# Diagnostico del modelo
cnf_confusion_matriz = metrics.confusion_matrix(Y_test, Y_pred)
print(cnf_confusion_matriz)
print("Precision: ",metrics.accuracy_score(Y_test, Y_pred)) # Acurycidad = proximidad entre el valor verdadero y el resultado medio que se obtendría aplicando el procedimiento experimental un gran número de veces
                                                            # La prediccion es en porcentaje decimal
                                                            
# Graficar los resultados
plt.scatter(X_test.values.ravel(), Y_test.values.ravel(), color='black', label='Datos')
plt.plot(X_test.values.ravel(), regresion_logistica.predict_proba(X_test)[:,1], color='red', label='Ajuste')
plt.xlabel('BMI')
plt.ylabel('Probabilidad de padecer diabetes')
plt.legend(loc='best')
plt.show()
