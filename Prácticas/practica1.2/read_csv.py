# pandas_demo.py
import pandas as pd
# 1. Leer un archivo CSV (asegúrate de tener 'earth-layers.csv' en la misma carpeta)
print("8. Leer CSV 'earth-layers.csv':")
layers = pd.read_csv('earth-layers.csv')
print(layers)
print("-"*40)

# 2. Calcular el grosor total de todas las capas
print("9. Grosor total de capas:")
print(layers['thickness'].sum())  # 6370

print("#Leer datos de tiempo")


clima = pd.read_csv('weather.csv')
print(clima)

print("#Leer datos de notas de estudiantes")

scores = pd.read_csv('scores.csv')
print(scores)