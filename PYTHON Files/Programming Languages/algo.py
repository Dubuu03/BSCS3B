import turtle
import colorsys
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)

# Set up the turtle
t = turtle.Turtle()
t.speed(0)  # Set the fastest drawing speed

# Number of shapes in the pattern
num_shapes = 200
shape_size = 30
shape_types = ["circle", "square", "triangle"]

for _ in range(num_shapes):
    # Randomly choose a shape type
    shape_type = random.choice(shape_types)

    # Calculate random position
    x = random.randint(-screen.window_width() // 2, screen.window_width() // 2)
    y = random.randint(-screen.window_height() // 2, screen.window_height() // 2)

    # Move turtle to the random position
    t.penup()
    t.goto(x, y)
    t.pendown()

    # Calculate the color using colorsys
    hue = random.random()  # Random hue
    r, g, b = colorsys.hsv_to_rgb(hue, 1.0, 1.0)  # Convert HSV to RGB
    t.fillcolor(r, g, b)  # Set the fill color
    t.pencolor("black")  # Set the pen color

    # Draw the shape
    if shape_type == "circle":
        t.begin_fill()
        t.circle(shape_size)
        t.end_fill()
    elif shape_type == "square":
        t.begin_fill()
        for _ in range(4):
            t.forward(shape_size)
            t.right(90)
        t.end_fill()
    elif shape_type == "triangle":
        t.begin_fill()
        for _ in range(3):
            t.forward(shape_size)
            t.right(120)
        t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open until closed manually
screen.mainloop()
