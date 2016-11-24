#import tkinter module
from tkinter import *
import random
class robot():
    def_init_(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.canvas = canvas
        self.ball = canvas.create_oval(self.x1, self.y1, self.x2, self.y2, fill = "red"
    def move_ball(self):
        d1 = random.randint(0,5)
        d2 = random.randint(2,3)
        self.canvas.move(self.ball, d1, d2)
        self.canvas.after(50, self.move_ball)
#initialise window and canvas
root = Tk()
root.title("ball simulator")
root.resizable(False,False)
canvas = canvas(root, width=500, height=500)
canvas.pack()
#animate balls
robot1 = canvas.create_oval(150,200,200,250)
robot2 = canvas.create_oval(150,200,200,250)
x1,y1,x2,y2 = canvas.coords(robot1)
x1,y1,x2,y2 = canvas.coords(robot2)
co1 = x1
co2 = y1
co3 = x2
co4 = y2
robot1 = robot(co1,co2,co3,co4)
robot.move_ball()
robot2 = robot(co1,co2,co3,co4)
robot.move_ball()
root.mainlood()
