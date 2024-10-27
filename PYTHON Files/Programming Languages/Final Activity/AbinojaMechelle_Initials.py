import turtle

# Initialize turtle
t = turtle.Turtle()
t.speed(0)
t.pensize(12)
s = turtle.Screen()
s.setup(width=1.0, height=1.0)
s.bgcolor("black")

# Starting position for 'MBA'
t.penup()
t.goto(-185, 150)
t.pendown()

c = ["White", "LightPink", "HotPink", "DeepPink", "Black", "Black", "LightPink", "HotPink", "DeepPink"]
a = 9
for i in range(a):
    t.color(c[i % 9])

    # Letter 'M'
    t.right(90)
    t.forward(280)
    t.back(280)
    t.left(10)
    t.forward(280)
    t.right(20)
    t.back(280)
    t.left(10)
    t.forward(280)

    # Move to the next letter
    t.penup()
    t.back(280)
    t.left(90)
    t.forward(50)
    t.pendown()

    # Letter 'B'
    t.right(90)
    t.forward(280)
    t.back(280)
    t.left(90)
    t.circle(-70, 180)
    t.left(90)
    t.left(90)
    t.circle(-70, 180)

    # Move to the next letter
    t.penup()
    t.left(90)
    t.back(280)
    t.left(90)
    t.forward(150)
    t.pendown()

    # Letter 'A'
    t.right(100)
    t.forward(280)
    t.back(280)
    t.right(-20)
    t.forward(280)
    t.back(50)
    t.right(100)
    t.forward(80)

    # Move to the next letter
    t.penup()
    t.back(80)
    t.right(80)
    t.forward(230)
    t.left(-280)
    t.forward(300)
    t.right(180)
    t.pendown()

# Move to position for 'MECHELLE ABINOJA'
t.color("Deep Pink")
t.speed(0)
t.penup()
t.goto(-205, -170)
t.pendown()
t.pensize(3)

# Functions to draw each letter
def draw_M():
    t.left(90)
    t.forward(20)
    t.right(135)
    t.forward(14.14)
    t.left(90)
    t.forward(14.14)
    t.right(135)
    t.forward(20)
    t.left(90)
    t.penup()
    t.forward(6)
    t.pendown()

def draw_E():
    t.forward(12)
    t.backward(12)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(8)
    t.backward(8)
    t.left(90)
    t.forward(10)
    t.right(90)
    t.forward(12)
    t.penup()
    t.forward(6)
    t.pendown()

def draw_C():
    t.forward(12)
    t.backward(12)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(12)
    t.penup()
    t.forward(6)
    t.pendown()

def draw_H():
    t.left(90)
    t.forward(20)
    t.backward(10)
    t.right(90)
    t.forward(12)
    t.left(90)
    t.forward(10)
    t.backward(20)
    t.penup()
    t.right(90)
    t.forward(6)
    t.pendown()

def draw_L():
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(12)
    t.penup()
    t.forward(6)
    t.pendown()

def draw_B():
    t.right(90)
    t.forward(20)
    t.left(90)
    t.circle(5, 180)
    t.left(180)
    t.circle(5, 180)
    t.penup()
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(4)
    t.pendown()

def draw_A():
    t.penup()
    t.left(60)
    t.pendown()
    t.forward(22)
    t.right(120)
    t.forward(22)
    t.backward(10)
    t.right(120)
    t.forward(10)
    t.penup()
    t.backward(10)
    t.left(270)
    t.forward(10)
    t.right(90)
    t.forward(4)
    t.pendown()

def draw_N():
    t.left(90)
    t.forward(20)
    t.right(135)
    t.forward(25)
    t.left(135)
    t.forward(20)
    t.penup()
    t.right(90)
    t.forward(4)
    t.pendown()

def draw_I():
    t.forward(12)
    t.backward(6)
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(6)
    t.backward(12)
    t.penup()
    t.forward(6)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(4)
    t.pendown()

def draw_J():
    t.penup()
    t.forward(10)
    t.pendown()
    t.backward(6)
    t.left(270)
    t.forward(18)
    t.right(45)
    t.forward(4)
    t.right(45)
    t.forward(4)
    t.right(45)
    t.forward(4)
    t.right(45)
    t.forward(6)
    t.penup()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.forward(8)
    t.pendown()

def draw_O():
    t.pendown()
    t.left(180)
    t.circle(10)
    t.penup()
    t.right(180)
    t.forward(14)
    t.pendown()

def draw_space():
    t.penup()
    t.forward(8)
    t.pendown()

# Drawing "MECHELLE B ABINOJA"
draw_M()
draw_E()
draw_C()
draw_H()
draw_E()
draw_L()
t.left(90)
t.forward(20)
t.right(90)
draw_L()
draw_E()
draw_space()
draw_space()
draw_space()
draw_B()
draw_space()
draw_space()
draw_space()
draw_A()
draw_space()
draw_B()
draw_space()
draw_I()
draw_space()
draw_N()
draw_space()
draw_space()
draw_O()
draw_space()
draw_J()
t.right(270)
draw_A()


#Drawing Flowers
def draw_bigflower():
    t.pensize(50)
    t.color("paleGreen")
    t.pendown()
    for _ in range(5):
        t.forward(80)
        t.right(144)  # Turning angle for a 5-point star
    t.penup()

# Move to the position for the star
t.penup()
t.goto(t.xcor() + -35, t.ycor() + 340)  # Adjusting position for star
t.setheading(30)  # Slightly slant the star
draw_bigflower()

def draw_smallflower():
    t.color("crimson")
    t.pendown()
    t.pensize(30)
    for _ in range(5):
        t.forward(50)
        t.right(144)  # Turning angle for a 5-point star
    t.penup()

# Move to the position for the star
t.penup()
t.goto(t.xcor() + 15, t.ycor() + 5)  # Adjusting position for star
t.setheading(30)  # Slightly slant the star
draw_smallflower()

def draw_smallerflower():
    t.pensize(10)
    t.color("White")
    t.pendown()
    for _ in range(5):
        t.forward(20)
        t.right(144)  # Turning angle for a 5-point star
    t.penup()

# Move to the position for the star
t.penup()
t.goto(t.xcor() + 60, t.ycor() + -70)  # Adjusting position for star
t.setheading(30)  # Slightly slant the star
draw_smallerflower()

# Hide the turtle and finish
t.hideturtle()
turtle.done()
