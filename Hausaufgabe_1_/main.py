#2.b.
def relativ_prime(a, b):
    while b > 0:
        a, b = b, a % b

    if a == 1:
        return a

def cea_mai_lunga_subsecventa_conectata(vector):
    subsecventa_maxima = 0

    aceasta_subsecventa = 1

    inceputul_subsecventei = 0

    for i in range(1, len(vector)):
        if relativ_prime(vector[i-1], vector[i]) == 1:
            aceasta_subsecventa = aceasta_subsecventa + 1
        else:
            if aceasta_subsecventa > subsecventa_maxima:
                subsecventa_maxima = aceasta_subsecventa
                inceputul_subsecventei = i - subsecventa_maxima
            aceasta_subsecventa = 1

    if aceasta_subsecventa > subsecventa_maxima:
        subsecventa_maxima = aceasta_subsecventa
        inceputul_subsecventei = len(vector) - subsecventa_maxima
        cea_mai_lunga_subsecventa = vector[inceputul_subsecventei: inceputul_subsecventei + subsecventa_maxima]
        return cea_mai_lunga_subsecventa
        print(cea_mai_lunga_subsecventa)
    else:
        cea_mai_lunga_subsecventa = vector[inceputul_subsecventei: inceputul_subsecventei + subsecventa_maxima]
        return cea_mai_lunga_subsecventa
        print(cea_mai_lunga_subsecventa)

sir_de_numere = input("Schreiben sie die Reihe von Zahlen bitte:")

afisare = sir_de_numere.split()

vector = [int(numar) for numar in afisare]

raspuns = cea_mai_lunga_subsecventa_conectata(vector)

print(f"Die langste zusammenhangende Teilfolge von die Reihe von Zahlen ist:\n{raspuns}")
