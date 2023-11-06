import math
def numere_repetate(lista):
    lista1 = lista[:]

    i = 0

    while i < len(lista1):
        element = lista1[i]

        if lista1.count(element) > 1:
            del lista1[i]
        else:
            i += 1

    return lista1

def numere_simetrice(lista):
    numar_perechi = 0

    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            numar1 = lista[i]
            numar2 = lista[j]

            if numar1 // 10 == numar2 % 10 and numar1 % 10 == numar2 // 10:
                numar_perechi += 1

    return numar_perechi

def cel_mai_mare_numar(lista):
    numere = [str(numar) for numar in lista]

    numere.sort(reverse = True)

    cel_mai_mare = ' '.join(numere)

    return cel_mai_mare

def cripteaza_lista1(lista):
    if len(lista) < 2:
        return lista

    cheie = lista[0]

    lista_criptata = [element ^ cheie for element in lista[1:]]

    return [cheie] + lista_criptata
'''
def cripteaza_lista2(lista, cheie):
    lista = ''.join(format(ord(caracter), '08b') for caracter in lista)

    cheie = ''.join(format(ord(caracter), '80b') for caracter in cheie)

    lista_criptata = ''.join('1' if l == c else '0' for l, c in zip(lista, cheie))

    return hex(int(lista_criptata, 2))

def cripteaza_lista3(lista, cheie):
    lista_criptata = [numar ^ cheie for numar in lista[1:]]

    return [cheie] + lista_criptata
'''
def numere(lista):
    lista1 = []

    for i in range(len(lista)):
            numar = lista[i]

            if numar // 10 == (numar % 10) * 3:
                lista1.append(numar)

    return lista1

def cea_mai_lunga(lista):
    if not lista:
        return []

    cea_mai_lunga_subsecventa = []

    cea_mai_lunga_subsecventa_temporara = []

    for numar in range(len(lista)):
        if lista[numar % 10] == lista[(numar + 1) // 10]:
            cea_mai_lunga_subsecventa_temporara.append(lista[numar])
            cea_mai_lunga_subsecventa_temporara.append(lista[numar + 1])
        else:
            cea_mai_lunga_subsecventa_temporara = [lista[numar]]

        if len(cea_mai_lunga_subsecventa_temporara) > len(cea_mai_lunga_subsecventa):
            cea_mai_lunga_subsecventa = cea_mai_lunga_subsecventa_temporara[:]

    return cea_mai_lunga_subsecventa
'''
def index1(from_, to_):
    indecsi = range(from_, to_ + 1)

    cmmmc = math.lcm(*indecsi)

    return cmmmc
'''
def index2(lista, from_, to_):
    if from_ < 0 or to_ >= len(lista) or from_ > to_:
        return None

    indecsi = lista[from_:to_ + 1]

    cmmmc = math.lcm(*indecsi)

    return cmmmc

lista = input("Introduceti va rog lista de numere cu 2 cifre:")

afisare = [int(numar) for numar in lista.split()]

rezultat1 = numere_repetate(afisare)

print(f"Lista in urma scoaterii elementelor care se repeta este:\n{rezultat1}")

rezultat2 = numere_simetrice(afisare)

print(f"Numarul de perechi cu elemente simetrice este:\n{rezultat2}")

rezultat3 = cel_mai_mare_numar(afisare)

print(f"Cel mai mare numar format din numerele listei este:\n{rezultat3}")

rezultat4 = cripteaza_lista1(afisare)

print(f"Lista criptata este:\n{rezultat4}")
'''
lista2 = lista[:]

cheie = (input("Introduceti va rog cheia pentru criptare:"))

rezultat5 = cripteaza_lista2(lista2, cheie)

print(f"Lista criptata este:\n{rezultat5}")

cheie1 = int(input("Introduceti va rog cheia pentru criptare:"))

rezultat6 = cripteaza_lista3(afisare, cheie1)

print(f"Lista criptata este:\n{rezultat6}")
'''
rezultat7 = numere(afisare)

print(f"Numerele care implinesc conditia x = y * 3 sunt:\n{rezultat7}")

rezultat8 = cea_mai_lunga(afisare)

print(f"Cea mai lunga subsecventa de tip 'Domino' este:\n{rezultat8}")

from_ = int(input("Introduceti va rog indexul 'from':"))

to_ = int(input("Introduceti va rog indexul 'to':"))
'''
rezultat9 = index1(from_, to_)

print(f"Cel mai mic multiplu comun intre numerele din intervalul [{from_},{to_}] este:\n{rezultat9}")
'''
from_ = int(input("Introduceti va rog indexul 'from':"))

to_ = int(input("Introduceti va rog indexul 'to':"))

rezultat10 = index2(afisare, from_, to_)

print(f"Cel mai mic multiplu comun intre numerele din intervalul [{from_},{to_}] ai listei este:\n{rezultat10}")