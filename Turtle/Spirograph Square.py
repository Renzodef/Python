# Python's version used: 3.8.2 64 bit
import turtle

# Title of the window
turtle.title("Spirograph Square!")
# Background color
turtle.bgcolor("black")
# Size of the pen
turtle.pensize(3)
# Speed of the pen
turtle.speed(0)

# Drawing
for _ in range (5):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
# Hiding the pen
turtle.hideturtle()

# This prevent the window to close after the draw is finished
turtle.done()