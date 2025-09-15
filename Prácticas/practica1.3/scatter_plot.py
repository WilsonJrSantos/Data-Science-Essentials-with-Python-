import matplotlib.pyplot as plt
import pandas as pd


df2 = pd.DataFrame({'x':[1,2,3,4], 'y':[2,4,1,3]})
plt.scatter(df2['x'], df2['y'])
plt.title("Gráfico de dispersión")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()