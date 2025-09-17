import pandas as pd

def analizar_mamiferos(path_csv):
    mammals = pd.read_csv(path_csv)
    print(">>> Mamíferos")
    print(mammals.head())

    # Jirafa
    giraffe = mammals.query('species == "giraffe"')
    print("\nJirafa:")
    print(giraffe)

    # Excepciones
    outliers = mammals.query('neck_vertebrae != 7')
    print("\nMamíferos que no tienen 7 vértebras:")
    print(outliers)
    print()
