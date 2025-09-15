### Pandas Cheatsheet en Español

---

#### **DataFrame()**

```python
pd.DataFrame()
```

* **Biblioteca:** pandas
* **Object class:** DataFrame
* Crea un nuevo objeto DataFrame.

**Ejemplos:**

```python
df = pd.DataFrame()
# dataframe vacío
df
# [Empty DataFrame]
```

```python
obj = {'ones':[1,2], 'tens':[10,20]}
df = pd.DataFrame(obj)
df
```

|   | ones | tens |
| - | ---- | ---- |
| 0 | 1    | 10   |
| 1 | 2    | 20   |

---

#### **read\_csv()**

```python
df = pd.read_csv('file.csv')
```

* **Método:** pandas
* **Descripción:** Carga un archivo CSV en un DataFrame.

**Ejemplos:**

```python
df = pd.read_csv('weather.csv')
df
```

| date    | city | temp | rain |
| ------- | ---- | ---- | ---- |
| 2023-01 | NY   | 32   | 0.5  |
| 2023-01 | LA   | 65   | 0    |

```python
scores = pd.read_csv('scores.csv')
scores
```

| id  | name | grade | score |
| --- | ---- | ----- | ----- |
| S01 | Ana  | 9     | 85    |
| S02 | Bob  | 10    | 92    |

---

#### **Series()**

```python
pd.Series()
```

* Crea un objeto Series (estructura 1D).

**Ejemplos:**

```python
vals = pd.Series([3,5,2,11])
vals
```

0 → 3
1 → 5
2 → 2
3 → 11

```python
df['price']
```

| item    | price |
| ------- | ----- |
| Book    | 7.99  |
| Pen     | 0.75  |
| Stapler | 8.25  |

Series *price*:
0 → 7.99
1 → 0.75
2 → 8.25

---

#### **head()**

```python
df.head(10)
```

* Obtiene las primeras N filas de un DataFrame.

```python
df.head(3)
```

| day | temp |
| --- | ---- |
| Mon | 22   |
| Tue | 25   |
| Wed | 20   |

---

#### **tail()**

```python
df.tail(10)
```

* Obtiene las últimas N filas de un DataFrame.

```python
df.tail(3)
```

| day | temp |
| --- | ---- |
| Fri | 23   |
| Sat | 26   |
| Sun | 24   |

---

#### **iloc\[]**

```python
df.iloc[int]
```

* Accede a una fila por posición entera (0-indexed).

```python
df.iloc[0]
```

day → Mon
temp → 22

---

#### **df\[column]**

```python
df['column']
```

* Devuelve una columna como Series.

```python
df['day']
```

0 → Mon
1 → Tue
2 → Wed

```python
df[['day','rain']]
```

| day | rain |
| --- | ---- |
| Mon | 0.5  |
| Tue | 0.2  |
| Wed | 0.8  |

---

#### **query()**

```python
df.query('col > 5')
```

* Filtra un DataFrame usando una condición.

```python
df.query('temp > 24')
```

| day | temp |
| --- | ---- |
| Tue | 25   |
| Fri | 28   |
| Sat | 25   |

```python
df.query('name == "Bob"')
```

| name | time |
| ---- | ---- |
| Bob  | 45   |

---

#### **eval()**

```python
df.eval('col + 5')
```

* Evalúa una expresión en cada fila.

```python
df.eval('dist + 1')
```

0 → 21
1 → 26

```python
delta = 10
df.eval('time + @delta')
```

0 → 15
1 → 13

---

#### **shape**

```python
df.shape
```

* Devuelve el tamaño del DataFrame `(filas, columnas)`.

---

#### **sum()**

```python
series.sum()
```

* Suma todos los valores de una Series.

```python
df['vals'].sum()
# 67.5
```

---

#### **mean()**

```python
series.mean()
```

* Calcula el promedio de una Series.

---

#### **min() / max() / median()**

```python
series.min()   # mínimo
series.max()   # máximo
series.median()# mediana
```

---

#### **loc\[]**

```python
df.loc[label]
```

* Obtiene una fila por etiqueta de índice.

```python
df.loc['Tue']
```

rain → 0

Agregar fila:

```python
df.loc['Sat'] = [30,4]
```

---

#### **set\_index()**

```python
df.set_index('column')
```

* Convierte una columna en el índice del DataFrame.

```python
df2 = df.set_index('day')
```

| day | temp |
| --- | ---- |
| Mon | 22   |
| Tue | 25   |


#### **iloc\[ ]**

```python
df.iloc[int]
```

* **Objeto:** DataFrame
* **Accesor:** `iloc`
* **Parámetro:** ubicación entera (posición de fila, comenzando en 0).
* **Función:** Obtiene una fila de un dataframe según su posición.

---

### **Ejemplo:**

```python
df.iloc[0]
```

**df:**

|   | day | temp |
| - | --- | ---- |
| 0 | Mon | 22   |
| 1 | Tue | 25   |
| 2 | Wed | 20   |
| 3 | Thu | 28   |
| 4 | Fri | 23   |

**Primera fila (posición 0):**

```
day     Mon
temp    22
```