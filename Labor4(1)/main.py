import turtle

# Dicționar pentru reprezentarea caracterelor
caractere = {
    'a': turtle.Turtle(),
    'b': turtle.Turtle(),
    'c': turtle.Turtle(),
    'd':
}

def deseneaza_caracter(caracter):
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()

    if caracter == 'a':
        turtle.forward(100)
        turtle.right(120)
        turtle.forward(100)
        turtle.backward(50)
        turtle.right(120)
        turtle.forward(50)
    elif caracter == 'b':
        turtle.circle(50, -180)
        turtle.right(180)
        turtle.circle(50, -180)
    elif caracter == 'c':
        turtle.circle(50, -360)
    # ... alte caractere ...

    turtle.hideturtle()
    turtle.done()

def adauga_caracter():
    while True:
        caracter_nou = input("Introduceti un caracter nou: ")

        if caracter_nou.lower() in caractere:
            print("Acest caracter exista deja. Va rugam introduceti alt caracter.")
        else:
            caractere[caracter_nou.lower()] = turtle.Turtle()
            print(f"Caracterul '{caracter_nou}' a fost adaugat cu succes!")
            break

def deseneaza_text(mesaj):
    if not mesaj:
        print("Nu s-a introdus niciun mesaj. Programul se termina.")
        return

    turtle.speed(1)
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()

    for caracter in mesaj:
        if caracter.lower() in caractere:
            turtle.clear()
            turtle.hideturtle()
            deseneaza_caracter(caracter.lower())
            turtle.penup()
            turtle.goto(-50, 0)
            turtle.pendown()

def deseneaza_cu_sagetile():
    turtle.speed(1)
    turtle.penup()
    turtle.goto(-50, 0)
    turtle.pendown()

    def inainte():
        turtle.forward(10)

    def inapoi():
        turtle.backward(10)

    def dreapta():
        turtle.right(45)

    def stanga():
        turtle.left(45)

    def ridica():
        turtle.penup()

    def coboara():
        turtle.pendown()

    turtle.onkey(inainte, 'w')
    turtle.onkey(inapoi, 's')
    turtle.onkey(dreapta, 'd')
    turtle.onkey(stanga, 'a')
    turtle.onkey(ridica, 'f')
    turtle.onkey(coboara, 'g')

    turtle.listen()
    turtle.mainloop()

def main():
    print("Turtle Paint v1.0")
    print("1. Deseneaza mesajul sau textul scris la tastatura.")
    print("2. Adauga un nou caracter.")

    while True:
        comanda = input("Alege o comanda (1 sau 2): ")

        if comanda == '1':
            mesaj = input("Introduceti mesajul sau textul: ")
            deseneaza_text(mesaj)
            break
        elif comanda == '2':
            adauga_caracter()
            print("Turtle Paint v1.0")
            print("1. Deseneaza mesajul sau textul scris la tastatura.")
            print("2. Adauga un nou caracter.")
        else:
            print("Comanda invalida. Va rugam introduceti 1 sau 2.")

    if not mesaj:
        return  # Programul se termina daca nu exista niciun mesaj

    deseneaza_cu_sagetile()
