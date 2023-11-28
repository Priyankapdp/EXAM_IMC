# Coded by Dr. Pantula Devi Priyanka, Date: 28-11-2023 (as part of a test)
# Senior Teaching Fellow - AI in Science - Technical Exercise 
# Making use of tkinter library for drawing on the screen but instead I could have used Matplotlib as well. 
# Both are NOT turtle graphics libraries.
import tkinter as tk
import math

# Using classes
class my_Turtle:
    def __init__(self, canvas, name, x=200, y=200):
        self.canvas = canvas
        self.name = name
        self.x = x
        self.y = y
        self.heading = 90  # Start facing north (90 degrees)
        self.pen_down = True
        self.color = "black"

    # The functions below allow use the commands given 
    def forward(self, distance):
        new_x = self.x + distance * round(math.cos(math.radians(self.heading)))
        new_y = self.y - distance * round(math.sin(math.radians(self.heading)))

        if self.pen_down:
            self.canvas.create_line(self.x, self.y, new_x, new_y, fill=self.color)

        self.x = new_x
        self.y = new_y

    def left(self, angle):
        self.heading += angle

    def right(self, angle):
        self.heading -= angle

    def penup(self):
        self.pen_down = False

    def pendown(self):
        self.pen_down = True

    def set_color(self, color):
        self.color = color

# The function below allows users to enter programs using the commands listed 
# above. It is possible to create multiple turtles and have each one move independently.
def interpret_command(command):
    command_parts = command.split()
    if command_parts[0] == 'turtle':
        name = command_parts[1]
        turtles[name] = my_Turtle(canvas, name)
    elif command_parts[0] == 'move':
        name, distance = command_parts[1], int(command_parts[2])
        turtles[name].forward(distance)
    elif command_parts[0] == 'left':
        name, angle = command_parts[1], int(command_parts[2])
        turtles[name].left(angle)
    elif command_parts[0] == 'right':
        name, angle = command_parts[1], int(command_parts[2])
        turtles[name].right(angle)
    elif command_parts[0] == 'pen':
        name, state = command_parts[1], command_parts[2]
        if state == 'up':
            turtles[name].penup()
        elif state == 'down':
            turtles[name].pendown()
    elif command_parts[0] == 'colour':
        name, color = command_parts[1], command_parts[2]
        turtles[name].set_color(color)
    else:
        print("Invalid command")

# Use a suitable library to draw on the screen in Python - tkinter or matplotlib
# Heading for the figure
root_plot = tk.Tk()
root_plot.title("Graphics Visualization (without Turtle library)")

canvas = tk.Canvas(root_plot, width=400, height=400, bg='white')
canvas.pack()

# Dictionary to store turtles
turtles = {}  

# Creating the initial turtle as per the language specifications
turtles['default'] = my_Turtle(canvas, 'default')

# The following program would draw a red square: 
program_commands = [
    "turtle tom",
    "colour tom red",
    "move tom 50",
    "left tom 90",
    "move tom 50",
    "left tom 90",
    "move tom 50",
    "left tom 90",
    "move tom 50"
]

for line in program_commands:
    interpret_command(line)

root_plot.mainloop()

# If using matplotlib - Uncomment the following lines and Comment lines 5, 75 - 79.
# import matplotlib.pyplot as plt
# plt.show()