from schimbarea_cuvintelor import schimba_cuvinte

#Aici este importata functia pentru schimbarea cuvintelor din celalalt modul pentru apelarea si folosirea acesteia.

nume_fisier = input("Introduceti numele fisierului care sa fie citit si in care sa se schimbe cuvintele:\n")

#Aici utilizatorul introduce numele fisierului care a fost creat inainte de executarea programului pentru a fi citit si
#sa se poata face in acesta schimbarea de cuvinte.

try:
    with open(nume_fisier, 'r') as file:
        text_initial = file.read()

    cuvant_vechi = input("Introduceti cuvantul pe care doriti sa-l schimbati:\n")

    if cuvant_vechi not in text_initial:
        print("Cuvantul nu a fost gasit.Va rog sa introduceti un cuvant aflat in textul dat.")

        exit()

    cuvant_nou = input("Introduceti cuvantul pe care doiriti sa-l inlocuiti:\n")

    text_schimbat = schimba_cuvinte(text_initial, cuvant_vechi, cuvant_nou)

    if text_schimbat == text_initial:

        print("Nu s-a facut nici-o schimbare")

    else:
        print(f"Textul schimbat:\n{text_schimbat}")

        numar_schimbari = text_initial.count(cuvant_vechi)

        print(f"Numarul de schimbari:{numar_schimbari}")

except FileNotFoundError:
    print(f"Fisierul {nume_fisier} nu a fost gasit.")

#Aici este verificat daca fisierul cu numele care a fost introdus de catre utilizator a fost gasit.Daca nu este gasit,
#programul afiseaza un mesaj care spune ca nu a gasit fisierul si se termina.Acesta trebuie sa fie pornit din nou
#pentru a se face inca o data executarea daca se ajunge in acest caz.Daca fisierul este gasit,se implementeaza
#schimbarea de cuvinte folosind 2 variabile unde utilizatorul trebuie sa introduca pentru prima cuvantul care sa fie
#inlocuit si pentru a doua cuvantul care sa-l inlocuiasca.Daca cuvantul care trebuie sa fie inlocuit nu se afla in text,
#programul se termina si roaga utilizatorul sa introduca un cuvant aflat in text cand este pornit din nou.Daca textul
#in urma schimbarii cuvintelor ramane la fel cum a fost,este afisat ca nu au fost facuta nici-o schimbare.Dupa introducerea
#cuvintelor,este apelata functia importata din celalalt modul pentru a face schimbarea intre acesteaa.La sfarsit,
#este afisat in consola textul cum apare schimbat cu cuvantul nou si este calculat si afisat numarul de schimbari ale
#cuvantului din text daca s-a gasit de mai multe ori in acesta.
