def cea_mai_lunga(lista):
    if not lista:
        return []

    cea_mai_lunga_subsecventa=[]

    cea_mai_lunga_subsecventa_temporara=[]

    for numar in range(len(lista)):
        if lista[numar%10] == lista[int(numar+1)//10]:
            cea_mai_lunga_subsecventa_temporara.append(lista[numar])
        else:
            cea_mai_lunga_subsecventa_temporara=[lista[numar]]

        if len(cea_mai_lunga_subsecventa_temporara)>len(cea_mai_lunga_subsecventa):
            cea_mai_lunga_subsecventa=cea_mai_lunga_subsecventa_temporara[:]

    return cea_mai_lunga_subsecventa

lista = input("Introduceti va rog lista de numere cu 2 cifre:")

afisare = [int(numar) for numar in lista.split()]

rezultat8=cea_mai_lunga(afisare)

print(f"Cea mai lunga subsecventa de tip 'Domino' este:\n{rezultat8}")