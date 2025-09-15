import matplotlib.pyplot as plt
import pandas as pd

# Primer gráfico
x = [1, 2, 3, 4, 5, 6]
y = [1, 8, 1, 8, 1, 8]
#plt.plot(x, y)
#plt.show()  # sin argumentos


#**Ejemplo sin `plt.show()`:** solo en cuadernos interactivos
x = [0, 50, 100]
y = [10, 1, 4]
#plt.plot(x, y, color='red')



# Segundo gráfico
df = pd.read_csv('earth-layers.csv')
print(df)

x = df['layer']
y = df['thickness']

plt.figure()  # nueva figura
plt.bar(x, y)
#plt.show()  # sin argumentos



