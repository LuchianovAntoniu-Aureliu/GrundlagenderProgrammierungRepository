#1.b.
def cea_mai_lunga_subsecventa_conectata(vector):
    if not vector:
        return []

    cea_mai_lunga_subsecventa = [vector[0]]

    cea_mai_lunga_subsecventa_temporara = [vector[0]]

    for numar in range(1, len(vector)):
        if vector[numar] > vector[numar-1]:
            cea_mai_lunga_subsecventa_temporara.append(vector[numar])
        else:
            cea_mai_lunga_subsecventa_temporara = [vector[numar]]

        if len(cea_mai_lunga_subsecventa_temporara) > len(cea_mai_lunga_subsecventa):
            cea_mai_lunga_subsecventa = cea_mai_lunga_subsecventa_temporara[:]

    return cea_mai_lunga_subsecventa

vector_de_numere = input("Schreiben sie ein Vektor von Zahlen bitte:")

impartire = vector_de_numere.split()

vector =[int(variabila_contor) for variabila_contor in impartire]

raspuns =cea_mai_lunga_subsecventa_conectata(vector)

print(f"Die langste asteigende zusammenhangende Teilfolge von die Vektor von Zahlen ist:\n{raspuns}")