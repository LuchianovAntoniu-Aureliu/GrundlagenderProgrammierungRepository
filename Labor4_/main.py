from citirea_fisierului import citeste_fisier
from verificarea_castigatorului import verifica_castigator

import random

#Aici sunt importate functiile din celalalte module pentru a fi apelate si folosite in acesta.

def alegerea_calculatorului():
    return random.choice(['foarfeca', 'piatra', 'hartie'])

#Aici este implementata functia pentru ca alegerea calculatorului dintre cele 3 in timpul jocului contra utilizatorul
#sa fie data la intamplare folosind functia random.choice() care apartine bibliotecii Pycharm.

print("Piatra,hartie,foarfeca")

deseneaza_foarfeca = citeste_fisier('foarfeca.txt')

deseneaza_piatra = citeste_fisier('piatra.txt')

deseneaza_hartia = citeste_fisier('hartie.txt')

puncte_utilizator = 0

puncte_calculator = 0

for variabila_contor in range(3):
    alegere_utilizator = input(f"Alege una dintre aceste 3:piatra,hartie,foarfeca.\n").lower()

    while alegere_utilizator not in ['foarfeca','piatra','hartie']:
        print(f"Alegere invalida.")

        alegere_utilizator = input(f"Alegeti din nou.\n").lower()

    print(f"Utilizatorul a ales:{alegere_utilizator}")

    if alegere_utilizator == 'foarfeca':
        print(deseneaza_foarfeca)

    elif alegere_utilizator == 'piatra':
        print(deseneaza_piatra)

    else:
        print(deseneaza_hartia)

    alegere_calculator = alegerea_calculatorului()

    print(f"Calculatorul a ales:{alegere_calculator}")

    if alegere_calculator == 'foarfeca':
        print(deseneaza_foarfeca)

    elif alegere_calculator == 'piatra':
        print(deseneaza_piatra)

    else:
        print(deseneaza_hartia)

    castigator = verifica_castigator(alegere_utilizator, alegere_calculator)

    print(f"Castigatorul rundei este:{castigator}")

    if castigator == 'Utilizatorul':
        puncte_utilizator += 1

    elif castigator == 'Calculatorul':
        puncte_calculator += 1

print("Jocul s-a incheiat")

if puncte_utilizator > puncte_calculator:
    print("Ai castigat meciul")

elif puncte_calculator > puncte_utilizator:
    print("Calculatorul a castigat meciul")

else:
    print("Meciul s-a terminat cu egalitate.")

#Aici este implementat jocul intre utilizator si calculator.Mai intai sunt deschise fisierele unde sunt salvate desenele
#care reprezinta optiunile si initializate 2 variabile care sa retina punctajul utilizatorului si calculatorului.Utilizatorul
#isi alege la inceput una dintre cele 3 optiuni penntru fiecare dintre cele 3 runde ale jocului si daca scrie altceva
#inafara de acestea,este rugat sa introduca din nou una dintre optiuni.Pentru fiecare dintre  ei sunt scrise conditii
#pentru a afisa desenul corespunzator optiunii alese.Calculatorul se foloseste de functia random.choice prin apelul ei din celalalt modul
#pentru a alege la intamplare una dintre optiuni.Pentru o runda castigata,se acorda un punct celui care a castigat-o.
#Daca calculatorul si utilizatorul folosesc aceeasi optiune,runda nu va fi castigata de niciunul si nu se acorda puncte.
#La sfarsit,sunt comparate prin conditii punctajele fiecaruia si utilizatorul este anuntat care dintre ei a castigat meciul
#sau daca s-a terminat cu egalitate.