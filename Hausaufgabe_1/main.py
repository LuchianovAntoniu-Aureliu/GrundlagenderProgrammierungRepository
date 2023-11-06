#2.a.

def este_prim(numar):
    if numar < 2:
        return False

    for i in range(2, int(numar/2) + 1):
        if numar % i == 0:
            return False
    return True

def primele_numere_prime(n):
    prime = []
    i = 2
    while len(prime) < n:
        if este_prim(i):
            prime.append(i)
        i += 1
    return prime

afisare = int(input("Schreiben sie ein Nummer bitte:"))

raspuns = primele_numere_prime(afisare)

print(f"Die ersten {afisare} Primzahlen sind:\n{raspuns}")