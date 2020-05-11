# Python's version used: 3.8.2 64 bit
from turtle import *

# Title of the window
title("Italian Flag!")
# Speed of the pen
speed(0)
# Size of the window
setup(800, 500)

# Move to start position
penup()
goto(-400, 250)
pendown()

# Green
color("green")
begin_fill()
forward(267)
right(90)
forward(500)
right(90)
forward(267)
end_fill()

# White
color("white")
begin_fill()
right(180)
forward(267)
left(90)
forward(500)
right(90)
forward(267)
right(90)
forward(500)
end_fill()

# Red
color("red")
begin_fill()
left(90)
forward(267)
left(90)
forward(500)
left(90)
forward(267)
end_fill()
hideturtle()

# This prevent the window to close after the draw is finished
done()