# Python's version used: 3.8.2 64 bit
import turtle

# Title of the window
turtle.title("Spirograph Circle!")
# Background color
turtle.bgcolor("black")
# Size of the pen
turtle.pensize(2)
# Speed of the pen
turtle.speed(0)

# Drawing
for _ in range (6):
    for colours in ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)
# Hiding the pen
turtle.hideturtle()

# This prevent the window to close after the draw is finished
turtle.done()