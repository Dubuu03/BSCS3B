import turtle

screen = turtle.Screen()
screen.title("Dustin Drix M. Narciso")
screen.bgcolor("#151F42")

t = turtle.Turtle()
t.color("#19E8ED")
t.pensize(8)
t.speed(20)

t.penup()
t.goto(-350,300)
t.pendown()

for i in range(2):
    t.forward(690)
    t.right(90)
    t.forward(590)
    t.right(90)

t.penup()
t.goto(-340,-150)
t.pendown()

t.color("#81726B")

t.begin_fill()
t.left(5)
t.forward(675)
t.right(95)
t.forward(192)
t.right(90)
t.forward(675)
t.right(90)
t.forward(135)
t.end_fill()

t.color("white")
t.penup()
t.goto(200,-90)
t.pendown()
t.right(90)

t.begin_fill()
for i in range(2):
    t.forward(133)
    t.right(90)
    t.forward(60)
    t.right(90)
t.end_fill()

t.color("#747474")
t.pensize(10)
t.back(5)
t.forward(138)
t.pensize(8)

# t.penup()
# t.right(180)
# t.goto(200,-90)
# t.pendown()
# t.right(90)
# t.forward(200)
turtle.done()