import matplotlib.pyplot as plt
import pandas as pd


df = pd.DataFrame({'day':['Mon','Tue','Wed','Thu'], 'temp':[22,25,20,21]})
plt.bar(df['day'], df['temp'])
plt.title("Temperatura por día")
plt.xlabel("Día")
plt.ylabel("Temperatura")
plt.show()