#1.a.
def este_prim(numar):
    if numar < 2:
        return False

    for i in range(2, int(numar/2) + 1):
        if numar % i == 0:
            return False
    return True

def numere_prime(n):
    prime = []

    for numar in range(2, n):
        if este_prim(numar):
            prime.append(numar)
    return prime

afisare = int(input("Schreiben sie ein naturliche Zahl bitte:"))

raspuns = numere_prime(afisare)

print(f"Die Primzahlen kleiner als die naturliche Zahl sind:\n{raspuns}")

