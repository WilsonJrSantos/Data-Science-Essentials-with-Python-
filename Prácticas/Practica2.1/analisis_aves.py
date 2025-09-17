import pandas as pd
import matplotlib.pyplot as plt

def analizar_aves(path_csv):
    birds = pd.read_csv(path_csv)
    print(">>> Aves")
    print(birds.head())

    # Distribución
    bird_counts = birds['neck_vertebrae'].value_counts().sort_index()
    print("\nDistribución de vértebras en aves:")
    print(bird_counts)

    bird_counts.plot.bar()
    plt.title("Distribución de vértebras cervicales en aves")
    plt.xlabel("Número de vértebras")
    plt.ylabel("Cantidad de especies")
    plt.tight_layout()
    plt.show()

    # Ave con máximo
    max_bird = birds.query('neck_vertebrae == neck_vertebrae.max()')
    print("\nAve con más vértebras:")
    print(max_bird)
    print()
