import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("🎃 Spooky Hello World! 👻")

# Create a turtle for drawing (this will be the one drawing the spooky "Hello World!")
spooky_turtle = turtle.Turtle()
spooky_turtle.color("white")
spooky_turtle.speed(0)
spooky_turtle.hideturtle()

# Function to draw a ghost
def draw_ghost(x, y):
    ghost = turtle.Turtle()
    ghost.penup()
    ghost.goto(x, y)
    ghost.color("white")
    ghost.begin_fill()
    ghost.circle(50)
    ghost.end_fill()

    ghost.goto(x-25, y-20)
    ghost.begin_fill()
    ghost.circle(25, steps=3)  # Draw ghost's body
    ghost.end_fill()

    ghost.goto(x-15, y+30)  # Eyes
    ghost.color("black")
    ghost.begin_fill()
    ghost.circle(5)
    ghost.end_fill()

    ghost.goto(x+15, y+30)
    ghost.begin_fill()
    ghost.circle(5)
    ghost.end_fill()

    ghost.hideturtle()

# Function to draw a bat
def draw_bat(x, y):
    bat = turtle.Turtle()
    bat.penup()
    bat.goto(x, y)
    bat.color("gray")
    bat.speed(10)
    bat.pendown()

    # Left wing
    bat.begin_fill()
    for _ in range(2):
        bat.circle(20, 90)
        bat.circle(20 // 2, 90)
    bat.end_fill()

    # Body
    bat.penup()
    bat.goto(x + 20, y)
    bat.pendown()
    bat.begin_fill()
    bat.circle(20)
    bat.end_fill()

    # Right wing
    bat.penup()
    bat.goto(x + 40, y)
    bat.pendown()
    bat.begin_fill()
    for _ in range(2):
        bat.circle(20, -90)
        bat.circle(20 // 2, -90)
    bat.end_fill()
    bat.hideturtle()

# Function to draw a pumpkin
def draw_pumpkin(x, y):
    pumpkin = turtle.Turtle()
    pumpkin.penup()
    pumpkin.goto(x, y)
    pumpkin.color("orange")
    pumpkin.begin_fill()
    pumpkin.circle(50)
    pumpkin.end_fill()

    # Eyes
    pumpkin.goto(x - 20, y + 20)
    pumpkin.color("black")
    pumpkin.begin_fill()
    pumpkin.circle(10)
    pumpkin.end_fill()

    pumpkin.goto(x + 20, y + 20)
    pumpkin.begin_fill()
    pumpkin.circle(10)
    pumpkin.end_fill()

    # Mouth
    pumpkin.goto(x - 30, y - 10)
    pumpkin.right(90)
    pumpkin.circle(30, 180)  # Curved mouth
    pumpkin.hideturtle()

# Function to display the "Hello World!" message in spooky style
def spooky_hello():
    spooky_turtle.penup()
    spooky_turtle.goto(-150, 150)
    spooky_turtle.pendown()
    spooky_turtle.color("white")
    spooky_turtle.write("Hello World!", font=("Chiller", 50, "bold"))  # Use spooky font
    spooky_turtle.hideturtle()

# Function to animate ghost and bat movement
def animate_ghosts_bats():
    for _ in range(10):
        # Random positions for ghost and bat
        ghost_x = random.randint(-300, 300)
        ghost_y = random.randint(-200, 200)
        bat_x = random.randint(-300, 300)
        bat_y = random.randint(-200, 200)

        # Draw ghost and bat at random positions
        draw_ghost(ghost_x, ghost_y)
        draw_bat(bat_x, bat_y)

        # Delay for animation effect
        time.sleep(0.5)

        # Clear the screen after each animation loop
        screen.clearscreen()
        screen.bgcolor("black")
        spooky_hello()  # Re-draw spooky message after each screen clear

# Draw initial pumpkin and spooky text
draw_pumpkin(0, -100)
spooky_hello()

# Animate ghosts and bats
animate_ghosts_bats()

# Hide the screen when finished
screen.mainloop()
