import turtle

pantalla = turtle.Screen()
pantalla.bgcolor("black")

t = turtle.Turtle()
t.pensize(5)
t.color("white")
t.speed(2)

def letra_J():
    t.penup()
    t.goto(-250, 0)
    t.pendown()
    t.forward(50)
    t.backward(25)
    t.right(90)
    t.forward(100)
    t.circle(25, 180)
    t.left(90)

def letra_O():
    t.penup()
    t.goto(-150, -50)
    t.pendown()
    t.circle(50)

def letra_H():
    t.penup()
    t.goto(-50, 0)
    t.pendown()
    t.right(90)
    t.forward(100)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(100)

def letra_A():
    t.penup()
    t.goto(75, 0)
    t.pendown()
    t.setheading(75)
    t.forward(105)
    t.right(150)
    t.forward(105)
    t.backward(52.5)
    t.right(105)
    t.forward(30)

def letra_N():
    t.penup()
    t.goto(175, 0)
    t.setheading(90)
    t.pendown()
    t.forward(100)
    t.goto(225, 0)
    t.setheading(90)
    t.forward(100)

# Dibujar cada letra
letra_J()
letra_O()
letra_H()
letra_A()
letra_N()

t.hideturtle()
pantalla.mainloop()
