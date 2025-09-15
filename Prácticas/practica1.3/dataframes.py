import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('earth-layers.csv')
print(df)

x = df['layer']
y = df['thickness']
plt.bar(x, y)


plt.bar( df['layer'], df['thickness'] )
plt.ylabel('Thickness (km)')
plt.title('Layers of the Earth')
plt.show()