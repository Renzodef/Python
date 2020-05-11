# Python's version used: 3.8.2 64 bit
import turtle as t

# Title of the window
t.title("Spirangle!")
# Background color
t.bgcolor("black")

# Drawing the spirangle
pen = t.Turtle()
pen.color("cyan")
for side in range(46):
    pen.forward(10 * side)
    pen.right(360 / 3)
pen.hideturtle()

# This prevent the window to close after the draw is finished
t.done()