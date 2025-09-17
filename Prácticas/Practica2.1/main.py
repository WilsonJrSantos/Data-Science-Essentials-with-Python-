from analisis_humano import analizar_humano
from analisis_mamiferos import analizar_mamiferos
from analisis_aves import analizar_aves

def main():
    print("=== Proyecto: Variación Esquelética ===\n")

    analizar_humano("adult-human-skeleton.csv")
    analizar_mamiferos("mammal-neck-bones.csv")
    analizar_aves("bird-neck-bones.csv")

if __name__ == "__main__":
    main()
