import turtle
'''
import multiprocessing 

from threading import Thread
'''
def dreptunghi():

    pen = turtle.Pen()

    pen.goto(0, 0)

    pen.pendown()

    pen.forward(100)

    pen.left(90)

    pen.forward(200)

    pen.left(90)

    pen.forward(100)

    pen.left(90)

    pen.forward(200)

    pen.left(90)

    pen.penup()

    pen.goto(25, 25)

    pen.pendown()

    pen.forward(25)

    pen.left(90)

    pen.forward(50)

    pen.left(90)

    pen.forward(25)

    pen.left(90)

    pen.forward(50)

    pen.left(90)

    pen.reset()

def inima():
    pen = turtle.Pen()

    pen.up()

    pen.goto(0, -200)

    pen.down()

    pen.left(140)

    pen.forward(220)

    for _ in range(200):
        pen.right(1)

        pen.forward(2)

    pen.left(119)

    for _ in range(200):
        pen.forward(2)

        pen.right(1)

    pen.forward(220)

    pen.reset()

def casa():
    casa1 = turtle.Pen()

    casa2 = turtle.Pen()

    casa1.up()

    casa2.up()

    casa1.goto(-200, 0)

    casa2.goto(200, 0)

    casa1.down()

    casa2.down()

    for _ in range(4):
        casa1.forward(200)

        casa1.left(90)

    for _ in range(4):
        casa2.forward(200)

        casa2.left(90)

    casa1.forward(50)

    casa2.forward(50)

    for _ in range(4):
        casa1.forward(100)

        casa1.left(90)

    for _ in range(4):
        casa2.forward(100)

        casa2.left(90)

    casa1.left(90)

    casa2.left(90)

    casa1.forward(50)

    casa2.forward(50)

    casa1.right(90)

    casa2.right(90)

    casa1.forward(25)

    casa2.forward(25)

    casa1.backward(25)

    casa2.backward(25)

    casa1.right(90)

    casa2.right(90)

    casa1.forward(50)

    casa2.forward(50)

    casa1.right(90)

    casa2.right(90)

    casa1.forward(50)

    casa2.forward(50)

    casa1.right(90)

    casa2.right(90)

    casa1.forward(200)

    casa2.forward(200)

    for _ in range(2):
        casa1.right(60)

        casa1.forward(115)

    for _ in range(2):
        casa2.right(60)

        casa2.forward(115)

    casa1.right(60)

    casa2.right(60)

    casa1.up()

    casa2.up()

    casa1.forward(75)

    casa2.forward(75)

    casa1.down()

    casa2.down()

    casa1.right(90)

    casa2.right(90)

    casa1.up()

    casa2.up()

    casa1.forward(25)

    casa2.forward(25)

    casa1.down()

    casa2.down()

    for _ in range(4):
        casa1.forward(50)

        casa1.right(90)

    for _ in range(4):
        casa2.forward(50)

        casa2.right(90)

    casa1.forward(25)

    casa2.forward(25)

    casa1.right(90)

    casa2.right(90)

    casa1.forward(50)

    casa2.forward(50)

    casa1.left(90)

    casa2.left(90)

    casa1.up()

    casa2.up()

    casa1.forward(75)

    casa2.forward(75)

    casa1.down()

    casa2.down()

    for _ in range(4):
        casa1.forward(50)

        casa1.left(90)

    for _ in range(4):
        casa2.forward(50)

        casa2.left(90)

    casa1.forward(25)

    casa2.forward(25)

    casa1.left(90)

    casa2.left(90)

    casa1.forward(50)

    casa2.forward(50)

    casa1.reset()

    casa2.reset()

'''
dreptunghi()

inima()

casa()
'''
def meniu():
    afisare = input("Alegeti desenul care vreti sa fie afisat pe ecran:"
                    "\n1 - Dreptunghiuri"
                    "\n2 - Inima"
                    "\n3 - Case"
                    "\nScrieti la tastatura cifra 0 pentru a opri programul."
                    "\n"
                   )

    if afisare == '1':
        dreptunghi()
        meniu()

    elif afisare == '2':
        inima()
        meniu()

    elif afisare == '3':
        casa()
        meniu()

    elif afisare == '0':
        return 0

    else:
        print("Va rog sa alegeti o valoare din cele afisate pe ecran.")
        meniu()

meniu()
'''
def deseneaza_casa(casa, pozitia):
    casa.speed(1)

    casa.penup()

    casa.goto(pozitia, 0)

    casa.pendown()

    for _ in range(4):
        casa.forward(100)

        casa.left(90)

t.setup(400, 200)

casa1 = t.Turtle()

casa2 = t.Turtle()

proces1 = multiprocessing.Process(target=deseneaza_casa, args=(casa1, -50))

proces2 = multiprocessing.Process(target=deseneaza_casa, args=(casa2, 150))

proces1.start()

proces2.start()

proces1.join()

proces2.join()

t.done()
'''
