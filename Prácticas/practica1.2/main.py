# pandas_demo.py
import pandas as pd

# 1. Crear un DataFrame vacío
print("1. DataFrame vacío:")
df = pd.DataFrame()
print(df)
print("-"*40)

# 2. Crear un DataFrame con columnas 'color' y 'radius'
print("2. DataFrame con datos:")
df['color'] = ['blue','red','yellow','green']
df['radius'] = [2,4,3,5]
print(df)
print("-"*40)

# 3. Calcular una nueva columna 'diameter'
print("3. Agregar columna 'diameter':")
df['diameter'] = df['radius'] * 2
print(df)
print("-"*40)

# 4. Cálculos rápidos con columnas
print("4. Cálculos rápidos:")
print("Mínimo de radius:", df['radius'].min())
print("Suma de diameter:", df['diameter'].sum())
print("Promedio de radius:", df['radius'].mean())
print("-"*40)

# 5. Acceder a columnas como Series
print("5. Columna 'color' como Series:")
print(df['color'])
print("-"*40)

# 6. Acceder a filas como Series usando iloc
print("6. Filas usando iloc:")
print("Primera fila:\n", df.iloc[0])
print("Segunda fila:\n", df.iloc[1])
print("Última fila:\n", df.iloc[-1])
print("-"*40)

# 7. Otras partes de un DataFrame
print("7. Información del DataFrame:")
print("Index:", df.index)
print("Columns:", df.columns)
print("Shape:", df.shape)
print("Número de filas:", df.shape[0])
print("Número de columnas:", df.shape[1])
print("-"*40)

