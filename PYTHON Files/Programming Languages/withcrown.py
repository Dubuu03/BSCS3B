import turtle

screen = turtle.Screen()
screen.title("Dustin Drix M. Narciso")
screen.bgcolor("#151F42")

t = turtle.Turtle()
t.pensize(8)
t.speed(10)


# D
t.color("#725ED6")
t.penup()
t.goto(-290,-250)
t.pendown()
t.left(90)
t.forward(200)
t.right(90)
t.forward(30)

t.circle(-90,160)
t.right(20)

t.color("#19E8ED")
t.penup()
t.goto(-260,-250)
t.pendown()
t.right(90)
t.forward(180)

t.penup()
t.goto(-290,-20)
t.pendown()
t.right(90)
t.forward(40)
t.circle(-117,170)
t.right(10)

# M
t.penup()
t.goto(-80,-20)
t.pendown()
t.left(90)
t.forward(230)
t.penup()

t.goto(-80,-20)
t.pendown()
t.left(30)
t.forward(150)
t.left(130)
t.forward(140)
t.right(70)

t.penup()
t.goto(80,-20)
t.pendown()
t.right(110)
t.forward(250)
t.left(20)

t.penup()
t.goto(80,-20)
t.pendown()
t.forward(230)

t.color("#725ED6")
t.penup()
t.goto(-60,-130)
t.pendown()
t.forward(120)


t.penup()
t.goto(60,-130)
t.pendown()
t.forward(120)

t.penup()
t.goto(-50,-20)
t.pendown()
t.left(90)
t.right(60)
t.forward(80)
t.right(30)

# N
t.color("#19E8ED")
t.penup()
t.goto(140,-20)
t.pendown()
t.forward(230)

t.penup()
t.goto(140,-20)
t.pendown()
t.left(20)
t.forward(245)

t.penup()
t.goto(180,-20)
t.pendown()
t.forward(245)
t.left(160)
t.forward(230)

t.color("#725ED6")
t.penup()
t.goto(160,-250)
t.pendown()
t.forward(120)

t.penup()
t.goto(240,-20)
t.pendown()
t.right(180)
t.forward(120)

# crown
t.pensize(4)
t.color("#E3A711","#19E8ED")

t.penup()
t.goto(-260,260)
t.pendown()
t.left(10)
a = 3
for i in range(5):
    t.pensize(a)
    t.forward(38)
    a=a+1

t.left(80)
t.forward(130)
t.left(100)
a=7
for i in range(5):
    t.pensize(a)
    t.forward(24)
    a=a-1

t.penup()
t.goto(-240,260)
t.pendown()
t.left(180)
a = 3
for i in range(5):
    t.pensize(a)
    t.forward(34)
    a=a+1

t.left(80)
t.forward(90)
t.left(100)
a = 7
for i in range(5):
    t.pensize(a)
    t.forward(20)
    a=a-1

# right
t.penup()
t.goto(240,260)
t.pendown()
t.left(160)
a = 3
for i in range(5):
    t.pensize(a)
    t.forward(38)
    a=a+1
t.right(80)
t.forward(130)
t.right(100)
a=7
for i in range(5):
    t.pensize(a)
    t.forward(24)
    a=a-1

t.penup()
t.goto(220,260)
t.pendown()
t.right(180)
a = 3
for i in range(5):
    t.pensize(a)
    t.forward(34)
    a=a+1
t.right(80)
t.forward(90)
t.right(100)
a=7
for i in range(5):
    t.pensize(a)
    t.forward(20)
    a=a-1

t.pensize(4)
# diamond
t.penup()
t.goto(-10,210)
t.pendown()
t.left(10)
t.begin_fill()
t.left(45)
t.forward(50)
for i in range(3):
    t.right(90)
    t.forward(50)
t.end_fill()

# center
t.penup()
t.goto(-20,190)
t.pendown()
t.left(45)
a=3
for i in range(5):
    t.pensize(a)
    t.forward(24)
    a=a+1

t.penup()
t.goto(0,190)
t.pendown()
a=3
for i in range(5):
    t.pensize(a)
    t.forward(24)
    a=a+1

t.pensize(5)
# below
t.penup()
t.goto(-260,20)
t.pendown()
t.left(90)
t.forward(500)

t.penup()
t.goto(-260,40)
t.pendown()
t.forward(500)

t.hideturtle()

turtle.done()

