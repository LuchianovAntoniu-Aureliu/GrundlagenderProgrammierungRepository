def verifica_castigator(alegere_utilizator, alegere_calculator):
    if alegere_utilizator == alegere_calculator:
        return 'Egalitate'

    elif (alegere_utilizator == 'foarfeca' and alegere_calculator == 'hartie') or\
         (alegere_utilizator == 'piatra' and alegere_calculator == 'foarfeca') or\
         (alegere_utilizator == 'hartie' and alegere_calculator == 'piatra'):
        return 'Utilizatorul'

    else:
        return 'Calculatorul'

#Aici este implementata functia pentru verificare castigatorului fiecarei runde prin folosirea conditiilor in care
#utilizatorul poate castiga contra calculatorul.Daca niciuna dintre acestea nu se indeplineste inseamna ca runda este
#castigata de catre calculator.

