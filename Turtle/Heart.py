# Python's version used: 3.8.2 64 bit
import turtle as t

# Title of the window
t.title("An Heart for You!")
# Background color
t.bgcolor("black")

# Creating the two pens
pen1 = t.Turtle()
pen2 = t.Turtle()

# Configuring the first pen
# The first color is the color of the pen
# The second is color we want to use to fill the figure
pen1.color("misty rose", "violet")
pen1.width(3)

# Configuring the second pen
pen2.color("violet", "misty rose")
pen2.width(3)

# Drawing the figure
pen1.begin_fill()
pen2.begin_fill()
pen1.goto(0, 100)
pen2.goto(0, 100)
pen1.goto(0, -50)
pen2.goto(0, -50)
pen2.left(40)
pen1.left(140)
pen2.forward(100)
pen1.forward(100)
for side in range(185):
    pen2.forward(1)
    pen1.forward(1)
    pen2.left(1)
    pen1.right(1)

# Filling the figure
pen2.end_fill()
pen1.end_fill()

# Deleting the arrows of the pens when the figure is finished
pen2.hideturtle()
pen1.hideturtle()

# Third and forth pen that write the sentence after the figure is finished
pen3 = t.Turtle()
pen3.speed(0)
pen3.color("deep pink")
pen3.width(3)
pen3.penup()
pen3.goto(0, 150)
pen3.pendown()
pen3.write('I Love You!', font=('Courier', 40, 'bold'), align='center')
pen3.penup()
pen3.goto(0, -150)
pen3.pendown()
pen3.write('Facciapi!', font=('Courier', 40, 'bold'), align='center')
pen3.hideturtle()

# This prevent the window to close after the draw is finished
t.done()