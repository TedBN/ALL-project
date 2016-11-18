#AI experiment in tkinter.

#Everything we need first gets imported.
from tkinter import *
from math import atan2,pi

#The first part builds a GUI and rectangles using Deyan's code as a base.
root = Tk()
arena = Canvas(root,width = 500,height = 500,bg = "white")
recPlayer = arena.create_rectangle(120,120,100,100)
recAI = arena.create_rectangle(380,380,400,400)

#With Deyan's code the the arrow keys will be used to move the player rectangle.
#Here the player functions are defined and binded to the arrow keys.
vx = 10                                             #These 2 variables determine the distance, which the player rectangle
vy = 10                                             #will move after an arrow key is pressed.
def moveUp(event):
    """This function moves the player up"""
    x1,y1,x2,y2 = arena.coords(recPlayer)
    arena.coords(recPlayer,x1,y1-vy,x2,y2-vy)
def moveDown(event):
    """This function moves the player down"""
    x1,y1,x2,y2 = arena.coords(recPlayer)
    arena.coords(recPlayer,x1,y1+vy,x2,y2+vy)
def moveLeft(event):
    """This function moves the player left"""
    x1,y1,x2,y2 = arena.coords(recPlayer)
    arena.coords(recPlayer,x1-vx,y1,x2-vx,y2)
def moveRight(event):
    """This function moves the player right"""
    x1,y1,x2,y2 = arena.coords(recPlayer)
    arena.coords(recPlayer,x1+vx,y1,x2+vx,y2)
arena.focus_set()
arena.bind("<Up>",moveUp)
arena.bind("<Down>",moveDown)
arena.bind("<Left>",moveLeft)
arena.bind("<Right>",moveRight)
arena.pack(padx = 10,pady = 10)

#This part is for the AI function definitions.
def calcAngle():
    """This function calculates what direction the player is relative to
    the AI in degrees. It calculates them counter-clockwise."""
    x1,y1,x2,y2 = arena.coords(recPlayer)
    x3,y3,x4,y4 = arena.coords(recAI)
    dx = x1-x3
    dy = y1-y3
    float(dx)
    float(dy)
    degrees = atan2(dx,dy)*(180/pi)
    degrees360 = degrees+180
    return degrees360
def moveUpAI():
    """This function moves the AI up"""
    x3,y3,x4,y4 = arena.coords(recAI)
    arena.coords(recAI,x3,y3-vy,x4,y4-vy)
def moveDownAI():
    """This function moves the AI down"""
    x3,y3,x4,y4 = arena.coords(recAI)
    arena.coords(recAI,x3,y3+vy,x4,y4+vy)
def moveLeftAI():
    """This function moves the AI left"""
    x3,y3,x4,y4 = arena.coords(recAI)
    arena.coords(recAI,x3-vx,y3,x4-vx,y4)
def moveRightAI():
    """This function moves the AI right"""
    x3,y3,x4,y4 = arena.coords(recAI)
    arena.coords(recAI,x3+vx,y3,x4+vx,y4)
root.mainloop()