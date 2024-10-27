import turtle

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
screen.title("Dustin Drix M. Narciso")
screen.bgcolor("Black")

t = turtle.Turtle()
t.pensize(8)
t.speed(5)

# D
t.color("green2")  # dark
t.penup()
t.goto(-290, -100)
t.pendown()
t.left(90)
t.forward(200)
t.right(90)
t.forward(50)
t.circle(-90, 160)
t.right(20)

t.color("salmon")  # light
t.penup()
t.goto(-275, -100)
t.pendown()
t.right(90)
t.forward(180)
t.penup()
t.goto(-280, 120)
t.pendown()
t.right(90)
t.forward(40)
t.circle(-110, 180)

# M
t.penup()  # light
t.goto(-80, 130)
t.pendown()
t.left(90)
t.forward(230)
t.penup()
t.goto(-80, 130)
t.pendown()
t.left(30)
t.forward(150)
t.left(130)
t.forward(140)
t.right(70)

t.penup()
t.goto(60, 130)
t.pendown()
t.right(110)
t.forward(150)
t.left(20)
t.penup()
t.goto(60, 130)
t.pendown()
t.forward(230)

t.color("green2")  # dark
t.penup()
t.goto(-65, 40)
t.pendown()
t.forward(140)

t.penup()
t.goto(45, 40)
t.pendown()
t.forward(140)

t.penup()
t.goto(-62, 130)
t.pendown()
t.left(90)
t.right(60)
t.forward(110)
t.right(30)

# N
t.color("salmon")  # light
t.penup()
t.goto(140, 130)
t.pendown()
t.forward(230)
t.penup()
t.goto(140, 130)
t.pendown()
t.left(20)
t.forward(245)

t.penup()
t.goto(160, 130)
t.pendown()
t.forward(245)
t.left(160)
t.forward(230)

t.color("green2")  # dark
t.penup()
t.goto(155, -100)
t.pendown()
t.forward(140)

t.penup()
t.goto(229, 130)
t.pendown()
t.right(180)
t.forward(140)

t.penup()
t.goto(300, 200)
t.pendown()
t.color("crimson")  # Planet color
t.begin_fill()
t.circle(60)
t.end_fill()

# Create a planet ring
t.penup()
t.pensize(5)
t.goto(290, 230)
t.pendown()
t.color("#9C9C9C")  # Ring color
t.width(8)
t.circle(75, 160)

def draw_star():
    t.pensize(1)
    t.color("gold")
    t.pendown()
    for _ in range(5):
        t.forward(20)
        t.right(144)
    t.penup()

# Move to the position for the star
t.penup()
t.goto(t.xcor() + 50, t.ycor() + -70)
t.setheading(30)
draw_star()

t.penup()
t.goto(t.xcor() + -280, t.ycor() + 60)
t.setheading(30)
draw_star()

t.penup()
t.goto(t.xcor() + 200, t.ycor() + -100)
t.setheading(30)
draw_star()

# Move to the position for the star
t.penup()
t.goto(t.xcor() + 30, t.ycor() + -70)
t.setheading(30)
draw_star()

t.penup()
t.goto(t.xcor() + -150, t.ycor() + 70)
t.setheading(30)
draw_star()

t.penup()
t.goto(t.xcor() + 50, t.ycor() + -80)
t.setheading(30)
draw_star()

t.goto(-210, -80)
t.penup()
t.goto(t.xcor() + 40, t.ycor() + -70)
t.setheading(30)
draw_star()

t.penup()
t.goto(t.xcor() + -200, t.ycor() + 60)
t.setheading(30)
draw_star()

t.goto(-550, -70)
t.penup()
t.goto(t.xcor() + 210, t.ycor() + -100)
t.setheading(30)
draw_star()

t.goto(-310, -70)
t.penup()
t.goto(t.xcor() + 50, t.ycor() + -70)
t.setheading(30)
draw_star()

t.goto(-180, -80)
t.penup()
t.goto(t.xcor() + -170, t.ycor() + 70)
t.setheading(30)
draw_star()

t.goto(-310, -150)
t.penup()
t.goto(t.xcor() + 50, t.ycor() + -70)
t.setheading(30)
draw_star()

t.goto(-620, -55)
t.penup()
t.goto(t.xcor() + 210, t.ycor() + -100)
t.setheading(30)
draw_star()

t.hideturtle()
turtle.done()
