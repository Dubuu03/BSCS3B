import turtle
from turtle import *
import colorsys

screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
speed(0)
pensize(3)
bgcolor("black")
hue = 0.33


for i in range(300):
    col = colorsys.hsv_to_rgb(hue, 1 - (i % 100) / 100.0, 1 - (i % 50) / 100.0)
    pencolor(col)
    hue = 0.33
    circle(5 - i, 100)
    lt(80)
    circle(5 - i, 100)
    rt(100)

hideturtle()
done()


