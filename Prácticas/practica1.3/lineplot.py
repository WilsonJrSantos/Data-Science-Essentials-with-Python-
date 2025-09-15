import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'day':['Mon','Tue','Wed','Thu'], 'temp':[22,25,20,21]})
plt.plot(df['day'], df['temp'], marker='o')
plt.title("Temperatura por día")
plt.xlabel("Día")
plt.ylabel("Temperatura")
plt.show()