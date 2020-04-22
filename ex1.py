import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Handling keypresses!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()


def h1():
    tess.forward(30)

def h2():
    tess.left(45)

def h3():
    tess.right(45)

def h4():
    wn.bye()

def change_red():
    tess.color("red")

def change_green():
    tess.color("green")

def change_blue():
    tess.color("blue")

def increase_pensize():
    if tess.pensize() >=1 or tess.pensize() <= 20:
        tess.pensize(tess.pensize()+1)

def decrese_pensize():
    if tess.pensize() >=1 or tess.pensize() <= 20:
        tess.pensize(tess.pensize()-1)

wn.onkey(h1,"Up")
wn.onkey(h2,"Left")
wn.onkey(h3,"Right")
wn.onkey(h4,"q")
wn.onkey(change_red,"r")
wn.onkey(change_green,"g")
wn.onkey(change_blue,"b")
wn.onkey(increase_pensize,"plus")
wn.onkey(decrese_pensize,"minus")
wn.listen()
wn.mainloop()