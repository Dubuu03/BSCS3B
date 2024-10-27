import turtle
import colorsys

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)

turtle.title("spiralTriangle")
turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")

n = 500  # Number of iterations
s = 2  # Initial step size
h = 0  # Initial hue value

for i in range(n):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    turtle.pencolor(c)
    turtle.forward(s)
    turtle.left(119)
    s += 2
    h += 1/n  # Increment the hue value to get a gradient effect

turtle.done()
