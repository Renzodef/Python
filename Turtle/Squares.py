# Python's version used: 3.8.2 64 bit
import turtle as t

# Title of the window
t.title("Squares!")
# Background color
t.bgcolor("black")

# Drawing the squares
pen = t.Turtle()
pen.color("cyan")
pen.speed(0)


def draw_square():
    for _ in range(4):
        pen.forward(100)
        pen.right(90)
        for _ in range(4):
            pen.forward(50)
            pen.right(90)


pen.penup()
pen.back(20)
pen.pendown()
for square in range(80):
    draw_square()
    pen.forward(5)
    pen.left(5)
pen.hideturtle()

# This prevent the window to close after the draw is finished
t.done()
