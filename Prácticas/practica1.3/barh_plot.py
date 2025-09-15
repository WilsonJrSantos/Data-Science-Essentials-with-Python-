import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame({'day':['Mon','Tue','Wed','Thu'], 'temp':[22,25,20,21]})

plt.barh(df['day'], df['temp'])
plt.title("Temperatura por día (horizontal)")
plt.xlabel("Temperatura")
plt.ylabel("Día")
plt.show()