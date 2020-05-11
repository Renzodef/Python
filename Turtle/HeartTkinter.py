# Python's version used: 3.8.2 64 bit
import tkinter as tk
from turtle import RawTurtle, TurtleScreen
import sys
import os

# These  lines are only to create a correct executable file with Pyinstaller
# by importing correctly the icon file.
# To do this go in the terminal in the folder of this file and type
# For Windows:
# pyinstaller --onefile --noconsole --add-data="Heart.ico;." --icon=Heart.ico HeartTkinter.py
if getattr(sys, 'frozen', False):
    icon_path = os.path.join(sys._MEIPASS, "Heart.ico")
else:
    try:
        os.chdir(os.path.dirname(__file__))
    except:
        pass
    finally:
        icon_path = "Heart.ico"

# Creating Window
root = tk.Tk()
# Window's title
root.title("An Heart for You!")
# Window's icon
root.iconbitmap(icon_path)
# Creating canvas
canvas = tk.Canvas(master = root, bg="black", width = 500, height = 500)
# The next 2 lines are mandatory if we want to change the background color
turtle_screen = TurtleScreen(canvas)
turtle_screen.bgcolor("black")
# This is mandatory if we want to use Turtle
canvas.pack()

# Creating the two pens
# Using RawTurtle is mandatory for the integration
pen1 = RawTurtle(turtle_screen)
pen2 = RawTurtle(turtle_screen)

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
pen3 = RawTurtle(turtle_screen)
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

# This prevent the window to be closed after it finishs the drawing
root.mainloop()