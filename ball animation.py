#import tkinter module
from tkinter import *
#import random module which generates random numbers
import random
#create class
class robot():
#define and initialise function
    def __init__(self,a1,b1,a2,b2):
        self.a1 = a1
        self.b1 = b1
        self.a2 = a2
        self.b2 = b2
#create class widget
        self.canvas = canvas
#create oval shape and add colour
        self.ball = canvas.create_oval(self.a1, self.b1, self.a2, self.b2, fill = "Blue")
#define function to move the ovals
    def move_ball(self):
#this module implements pseudo-random number generators for various distributions
        c1 = random.randint(0,9)
        c2 = random.randint(0,9)
        self.canvas.move(ALL, c1, c2)
        self.canvas.after(200, self.move_ball)
#create window and canvas name
root = Tk()
root.title("Ball simulator")
root.resizable(False,False)
#create canvas size
canvas = Canvas(root, width = 500, height = 500)
canvas.pack()
#assign the objects coordinates
robot1 = canvas.create_oval(150,200,200,250)
robot2 = canvas.create_oval(150,200,200,250)
a1,b1,a2,b2 = canvas.coords(robot1)
x1,y1,x2,y2 = canvas.coords(robot2)
co1 = a1
co2 = b1
co3 = a2
co4 = b2
robot1 = robot(co1,co2,co3,co4)
robot1.move_ball()
robot2 = robot(co1,co2,co3,co4)
robot2.move_ball()
root.mainloop()
