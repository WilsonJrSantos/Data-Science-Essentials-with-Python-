import pandas as pd

# ----------------------------
# 1️⃣ DataFrame vacío y desde diccionario
# ----------------------------
print("--- DataFrame vacío ---")
df_empty = pd.DataFrame()
print(df_empty)

print("\n--- DataFrame desde diccionario ---")
obj = {'ones':[1,2], 'tens':[10,20]}
df = pd.DataFrame(obj)
print(df)

# ----------------------------
# 2️⃣ Leer CSV
# ----------------------------
print("\n--- Leer weather.csv ---")
weather = pd.read_csv('weather.csv')
print(weather)

print("\n--- Leer scores.csv ---")
scores = pd.read_csv('scores.csv')
print(scores)

print("\n--- Leer price.csv ---")
prices = pd.read_csv('price.csv')
print(prices)

print("\n--- Leer days.csv ---")
days = pd.read_csv('days.csv')
print(days)

# ----------------------------
# 3️⃣ Series
# ----------------------------
print("\n--- Series ---")
vals = pd.Series([3,5,2,11])
print(vals)

print("\n--- Columna como Series ---")
print(prices['price'])

# ----------------------------
# 4️⃣ head() y tail()
# ----------------------------
print("\n--- head(3) ---")
print(days.head(3))

print("\n--- tail(3) ---")
print(days.tail(3))

# ----------------------------
# 5️⃣ iloc
# ----------------------------
print("\n--- iloc[0] ---")
print(days.iloc[0])

# ----------------------------
# 6️⃣ Acceso a columnas
# ----------------------------
print("\n--- df['column'] ---")
print(days['day'])

print("\n--- df[['day','rain']] ---")
print(days[['day','rain']])

# ----------------------------
# 7️⃣ query
# ----------------------------
print("\n--- query temp > 24 ---")
print(days.query('temp > 24'))

print("\n--- query name == 'Bob' ---")
print(scores.query('name == "Bob"'))

# ----------------------------
# 8️⃣ eval
# ----------------------------
print("\n--- eval ---")
dist_df = pd.DataFrame({'dist':[20,25]})
print(dist_df.eval('dist + 1'))

delta = 10
time_df = pd.DataFrame({'time':[5,3]})
print(time_df.eval('time + @delta'))

df = pd.DataFrame({'radius': [2, 3, 4]})

# Creamos la columna diameter usando eval
df.eval('diameter = radius * 2', inplace=True)
print(df)

df = pd.DataFrame({'numeros': [3, 6, 9]})

# Creamos la columna cuadrados usando eval
df.eval('cuadrados = numeros** 2', inplace=True)
print(df)

# ----------------------------
# 9️⃣ shape, sum, mean, min, max, median
# ----------------------------
print("\n--- shape ---")
print(days.shape)

print("\n--- sum ---")
print(prices['price'].sum())

print("\n--- mean ---")
print(prices['price'].mean())

print("\n--- min / max / median ---")
print(prices['price'].min(), prices['price'].max(), prices['price'].median())

# ----------------------------
# 10️⃣ loc
# ----------------------------
day_df = days.set_index('day')[['temp','rain']]
print("\n--- loc['Tue'] ---")
print(day_df.loc['Tue'])

# agregar fila
day_df.loc['NextDay'] = [30,4]
print("\n--- Agregar fila ---")
print(day_df)

# ----------------------------
# 11️⃣ set_index
# ----------------------------
print("\n--- set_index ---")
day_df2 = days.set_index('day')
print(day_df2)



# ----------------------------
# 5️⃣ iloc - más ejemplos
# ----------------------------
print("\n--- iloc[0] primera fila ---")
print(days.iloc[0])

print("\n--- iloc[2] tercera fila ---")
print(days.iloc[2])

print("\n--- iloc[-1] última fila ---")
print(days.iloc[-1])

print("\n--- iloc[0:3] primeras 3 filas ---")
print(days.iloc[0:3])

print("\n--- iloc[:, 0] primera columna (day) ---")
print(days.iloc[:, 0])

print("\n--- iloc[0, 1] valor fila 0 columna 1 (temp del primer día) ---")
print(days.iloc[0, 1])
