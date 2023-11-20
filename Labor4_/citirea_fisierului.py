def citeste_fisier(nume_fisier):
    with open(nume_fisier, 'r') as file:
        return file.read()

#Aici este implementata functia pentru citirea fisierelor de tip text care contin desenele pietrei,hartiei
#si a foarfecii ca sa poata fi afisate in consola in timpul executarii programului.
