import turtle

screen = turtle.Screen()
screen.title("Dustin Drix M. Narciso")
screen.bgcolor("#151F42")

t = turtle.Turtle()
t.pensize(8)
t.speed(5)


# D
t.color("#725ED6") #dark
t.penup()
t.goto(-290,-100)
t.pendown()
t.left(90)
t.forward(200)
t.right(90)
t.forward(30)

t.circle(-90,160)
t.right(20)

t.color("#19E8ED") #light
t.penup()
t.goto(-260,-100)
t.pendown()
t.right(90)
t.forward(180)

t.penup()
t.goto(-290,130)
t.pendown()
t.right(90)
t.forward(40)
t.circle(-117,170)
t.right(10)

# M
t.penup()  #light
t.goto(-80,130)
t.pendown()
t.left(90)
t.forward(230)
t.penup()

t.goto(-80,130)
t.pendown()
t.left(30)
t.forward(150)
t.left(130)
t.forward(140)
t.right(70)

t.penup()
t.goto(80,130)
t.pendown()
t.right(110)
t.forward(250)
t.left(20)

t.penup()
t.goto(80,130)
t.pendown()
t.forward(230)

t.color("#725ED6") #dark
t.penup()
t.goto(-60,20)
t.pendown()
t.forward(120)


t.penup()
t.goto(60,20)
t.pendown()
t.forward(120)

t.penup()
t.goto(-50,130)
t.pendown()
t.left(90)
t.right(60)
t.forward(80)
t.right(30)

# N
t.color("#19E8ED") #light
t.penup()
t.goto(140,130)
t.pendown()
t.forward(230)

t.penup()
t.goto(140,130)
t.pendown()
t.left(20)
t.forward(245)

t.penup()
t.goto(180,130)
t.pendown()
t.forward(245)
t.left(160)
t.forward(230)

t.color("#725ED6") #dark
t.penup()
t.goto(160,-100)
t.pendown()
t.forward(120)

t.penup()
t.goto(240,130)
t.pendown()
t.right(180)
t.forward(120)

t.hideturtle()
turtle.done()


