import turtle
import colorsys

turtle.bgcolor("black")
screen = turtle.Screen()
screen.setup(width=1.0, height=1.0)
turtle.speed(0)
turtle.hideturtle()

num_shades = 9
colors = []

for i in range(num_shades):
    hue = 0.9 - i * (0.3 / (num_shades - 1))
    lightness = 0.4 + (i * 0.05)
    r, g, b = colorsys.hls_to_rgb(hue, lightness, 1.0)
    colors.append((r, g, b))

for i in range(30):
    for c in colors:
        turtle.color(c)
        turtle.circle(200 - i, 100)
        turtle.up()
        turtle.lt(90)
        turtle.forward(10)
        turtle.down()
        turtle.circle(200 - i, 100)
        turtle.rt(60)
        turtle.up()
        turtle.backward(10)
        turtle.down()

turtle.mainloop()
