# Python's version used: 3.8.2 64 bit
import turtle as t

# Title of the window
t.title("Spiral!")
# Background color
t.bgcolor("black")


# Drawing the spiral
def spiral(sides, trun, color, width):
    pen = t.Turtle()
    pen.color(color)
    pen.width(width)
    pen.speed(0)
    for n in range(sides):
        pen.forward(n)
        pen.right(trun)
    pen.hideturtle()


spiral(150, 45, "cyan", 5)

# This prevent the window to close after the draw is finished
t.done()