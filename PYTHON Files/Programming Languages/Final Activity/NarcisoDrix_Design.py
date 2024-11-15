import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.title('Pikachu')
turtle.bgcolor("#F5DEB3")
t = turtle.Turtle()
t.pensize(3)
t.speed(9)

# Body
t.fillcolor('#F6D02F')
t.begin_fill()
t.penup()
t.circle(130, 40)
t.pendown()
t.circle(100, 105)
t.left(180)
t.circle(-100, 5)

t.setheading(20)
t.circle(300, 30)
t.circle(30, 50)
t.setheading(190)
t.circle(300, 36)

t.setheading(150)
t.circle(150, 70)

t.setheading(200)
t.circle(300, 40)
t.circle(30, 50)
t.setheading(20)
t.circle(300, 35)

t.setheading(240)
t.circle(105, 95)
t.left(180)
t.circle(-105, 5)

t.setheading(210)
t.circle(500, 18)
t.setheading(200)
t.forward(10)
t.setheading(280)
t.forward(7)
t.setheading(210)
t.forward(10)
t.setheading(300)
t.circle(10, 80)
t.setheading(220)
t.forward(10)
t.setheading(300)
t.circle(10, 80)
t.setheading(240)
t.forward(12)
t.setheading(0)
t.forward(13)
t.setheading(240)
t.circle(10, 70)
t.setheading(10)
t.circle(10, 70)
t.setheading(10)
t.circle(300, 18)

t.setheading(75)
t.circle(500, 8)
t.left(180)
t.circle(-500, 15)
t.setheading(250)
t.circle(100, 65)

t.setheading(320)
t.circle(100, 5)
t.left(180)
t.circle(-100, 5)
t.setheading(220)
t.circle(200, 20)
t.circle(20, 70)

t.setheading(60)
t.circle(-100, 20)
t.left(180)
t.circle(100, 20)
t.setheading(300)
t.circle(10, 70)

t.setheading(60)
t.circle(-100, 20)
t.left(180)
t.circle(100, 20)
t.setheading(10)
t.circle(100, 60)

t.setheading(180)
t.circle(-100, 10)
t.left(180)
t.circle(100, 10)
t.setheading(5)
t.circle(100, 10)
t.circle(-100, 40)
t.circle(100, 35)
t.left(180)
t.circle(-100, 10)

t.setheading(290)
t.circle(100, 55)
t.circle(10, 50)

t.setheading(120)
t.circle(100, 20)
t.left(180)
t.circle(-100, 20)

t.setheading(0)
t.circle(10, 50)

t.setheading(110)
t.circle(100, 20)
t.left(180)
t.circle(-100, 20)

t.setheading(30)
t.circle(20, 50)

t.setheading(100)
t.circle(100, 40)

t.setheading(200)
t.circle(-100, 5)
t.left(180)
t.circle(100, 5)
t.left(30)
t.circle(100, 75)
t.right(15)
t.circle(-300, 21)
t.left(180)
t.circle(300, 3)

t.setheading(43)
t.circle(200, 60)

t.right(10)
t.forward(10)

t.circle(5, 160)
t.setheading(90)
t.circle(5, 160)
t.setheading(90)

t.forward(10)
t.setheading(90)
t.circle(5, 180)
t.forward(10)

t.left(180)
t.left(20)
t.forward(10)
t.circle(5, 170)
t.forward(10)
t.setheading(240)
t.circle(50, 30)

t.end_fill()
t.penup()
t.goto(130, 125)
t.pendown()
t.setheading(-20)
t.forward(5)
t.circle(-5, 160)
t.forward(5)

t.penup()
t.goto(166, 130)
t.pendown()
t.setheading(-90)
t.forward(3)
t.circle(-4, 180)
t.forward(3)
t.setheading(-90)
t.forward(3)
t.circle(-4, 180)
t.forward(3)

t.penup()
t.goto(168, 134)
t.pendown()
t.fillcolor('#F6D02F')
t.begin_fill()
t.setheading(40)
t.forward(200)
t.setheading(-80)
t.forward(150)
t.setheading(210)
t.forward(150)
t.left(90)
t.forward(100)
t.right(95)
t.forward(100)
t.left(110)
t.forward(70)
t.right(110)
t.forward(80)
t.left(110)
t.forward(30)
t.right(110)
t.forward(32)

t.right(106)
t.circle(100, 25)
t.right(15)
t.circle(-300, 2)
t.setheading(30)
t.forward(40)
t.left(100)
t.forward(70)
t.right(100)
t.forward(80)
t.left(100)
t.forward(46)
t.setheading(66)
t.circle(200, 38)
t.right(10)
t.forward(10)
t.end_fill()

# Left Hand
t.fillcolor('#923E24')
t.penup()
t.goto(126.82, -156.84)
t.pendown()
t.begin_fill()

t.setheading(30)
t.forward(40)
t.left(100)
t.forward(40)
t.pencolor('#923e24')
t.setheading(-30)
t.forward(30)
t.left(140)
t.forward(20)
t.right(150)
t.forward(20)
t.left(150)
t.forward(20)
t.right(150)
t.forward(20)
t.left(130)
t.forward(18)
t.pencolor('#000000')
t.setheading(-45)
t.forward(67)
t.right(110)
t.forward(80)
t.left(110)
t.forward(30)
t.right(110)
t.forward(32)
t.right(106)
t.circle(100, 25)
t.right(15)
t.circle(-300, 2)
t.end_fill()

# Cap
t.penup()
t.goto(-134.07, 147.81)
t.pendown()
t.fillcolor('#CD0000')
t.begin_fill()
t.setheading(200)
t.circle(400, 7)
t.left(180)
t.circle(-400, 30)
t.circle(30, 60)
t.forward(50)
t.circle(30, 45)
t.forward(60)
t.left(5)
t.circle(30, 70)
t.right(20)
t.circle(200, 70)
t.circle(30, 60)
t.forward(70)
t.right(35)
t.forward(50)
t.circle(8, 100)
t.end_fill()
t.penup()
t.goto(-168.47, 185.52)
t.pendown()
t.setheading(36)
t.circle(-270, 54)
t.left(180)
t.circle(270, 27)
t.circle(-80, 98)

t.fillcolor('#ffffff')
t.begin_fill()
t.left(180)
t.circle(80, 197)
t.left(58)
t.circle(200, 45)
t.end_fill()

t.penup()
t.goto(-58, 270)
t.pendown()
t.pencolor('#228B22')
t.dot(35)

t.penup()
t.goto(-30, 280)
t.pendown()
t.fillcolor('#228B22')
t.begin_fill()
t.setheading(100)
t.circle(30, 180)
t.setheading(190)
t.forward(15)
t.setheading(100)
t.circle(-45, 180)
t.right(90)
t.forward(15)
t.end_fill()
t.pencolor('#000000')

# Mouth
t.penup()
t.goto(-5, 25)
t.pendown()
t.fillcolor('#88141D')
t.begin_fill()
t.setheading(190)

a = 0.7
l1 = []
l2 = []
for i in range(28):
    a += 0.1
    t.right(3)
    t.forward(a)
    l1.append(t.position())

t.penup()
t.goto(-5, 25)
t.pendown()
t.setheading(10)

a = 0.7
for i in range(28):
    a += 0.1
    t.left(3)
    t.forward(a)
    l2.append(t.position())

t.setheading(10)
t.circle(50, 15)
t.left(180)
t.circle(-50, 15)

t.circle(-50, 40)
t.setheading(233)
t.circle(-50, 55)
t.left(180)
t.circle(50, 12.1)
t.end_fill()

t.penup()
t.goto(17, 54)
t.pendown()
t.fillcolor('#DD716F')
t.begin_fill()
t.setheading(145)
t.circle(40, 86)
t.penup()

for pos in reversed(l1[:20]):
    t.goto(pos[0], pos[1]+1.5)
for pos in l2[:20]:
    t.goto(pos[0], pos[1]+1.5)
t.pendown()
t.end_fill()

t.penup()
t.goto(-17, 94)
t.pendown()
t.setheading(8)
t.forward(4)
t.backward(8)

# Left cheek
turtle.tracer(False)
t.penup()
t.goto(-126, 32)
t.pendown()
t.setheading(300)
t.fillcolor('#DD4D28')
t.begin_fill()
a = 2.3
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        t.left(3)
        t.forward(a)
    else:
        a += 0.05
        t.left(3)
        t.forward(a)
t.end_fill()
turtle.tracer(True)

# Right cheek
turtle.tracer(False)
t.penup()
t.goto(107, 63)
t.pendown()
t.setheading(60)
t.fillcolor('#DD4D28')
t.begin_fill()
a = 2.3
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
        t.left(3)
        t.forward(a)
    else:
        a += 0.05
        t.left(3)
        t.forward(a)
t.end_fill()
turtle.tracer(True)

# Left ear
t.penup()
t.goto(-250, 100)
t.pendown()
t.fillcolor('#000000')
t.begin_fill()
t.setheading(330)
t.circle(100, 35)
t.setheading(219)
t.circle(-300, 19)
t.setheading(110)
t.circle(-30, 50)
t.circle(-300, 10)
t.end_fill()

# Right ear
t.penup()
t.goto(140, 270)
t.pendown()
t.fillcolor('#000000')
t.begin_fill()
t.setheading(300)
t.circle(-100, 30)
t.setheading(35)
t.circle(300, 15)
t.circle(30, 50)
t.setheading(190)
t.circle(300, 17)
t.end_fill()

# Left eye
t.penup()
t.goto(-85, 90)
t.pendown()
t.setheading(0)
t.fillcolor('#333333')
t.begin_fill()
t.circle(22)
t.end_fill()

t.penup()
t.goto(-85, 100)
t.pendown()
t.fillcolor('#000000')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(-79, 112)
t.pendown()
t.fillcolor('#ffffff')
t.begin_fill()
t.circle(10)
t.end_fill()

# Right eye
t.penup()
t.goto(50, 110)
t.pendown()
t.setheading(0)
t.fillcolor('#333333')
t.begin_fill()
t.circle(22)
t.end_fill()

t.penup()
t.goto(50, 120)
t.pendown()
t.fillcolor('#000000')
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(44, 132)
t.pendown()
t.fillcolor('#ffffff')
t.begin_fill()
t.circle(10)
t.end_fill()

t.hideturtle()

turtle.mainloop()
