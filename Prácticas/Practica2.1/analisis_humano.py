import pandas as pd

def analizar_humano(path_csv):
    df = pd.read_csv(path_csv)
    print(">>> Esqueleto humano")
    print(df.head())
    print(f"Total de huesos: {len(df)}\n")

    # Conteo por región
    region_counts = df['region'].value_counts()
    print("Huesos por región:")
    print(region_counts)

    # Proporción manos y pies
    prop_manos_pies = (region_counts['hand'] + region_counts['foot']) / len(df)
    print(f"\nProporción manos+pies: {prop_manos_pies:.2%}\n")

    # Bebés (fusión)
    total_huesos_bebe = df['fused_from'].sum()
    print(f"Huesos en bebés: {total_huesos_bebe}\n")

    # Cuello humano
    cuello = df.query('region == "neck"')
    print("Huesos en el cuello humano:")
    print(cuello)
    print()
