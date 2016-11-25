#AI experiment in tkinter.

#Everything we need first gets imported.
from tkinter import *
from math import atan2,pi

#The first part builds a GUI and rectangles using Deyan's code as a base.
root = Tk()
arena = Canvas(root,width = 500,height = 500,bg = "white")
recPlayer = arena.create_rectangle(120,120,100,100)
recAI = arena.create_rectangle(380,380,400,400)

#These 2 variables determine the distance, which the rectangles
#will move after an arrow key is pressed/tick has passed.
vx = 10
vy = 10

#These values are used to determine the player's borders.
x_max = 500                                             
x_min = 0
y_max = 480
y_min = 0

#With Deyan's code the the arrow keys will be used to move the player rectangle.
#Here the player functions are defined and binded to the arrow keys.
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
def coordCheck(event):
    """This function returns the player's current position on the canvas.
    It is called by left clicking on the canvas."""
    #Note: Used for debugging and will be removed in future.
    x1,y1,x2,y2 = arena.coords(recPlayer)
    print(x1,y1)
arena.focus_set()
arena.bind("<Up>",moveUp)
arena.bind("<Down>",moveDown)
arena.bind("<Left>",moveLeft)
arena.bind("<Right>",moveRight)
arena.bind("<Button-1>",coordCheck)
arena.pack(padx = 10,pady = 10)

#This part is for the AI function definitions and calls.
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
def ai():
    """This function acts as the AI's main loop. It uses the calcAngle function to get
    the player's position and moves the AI towards the player. This function then calls itself
    again once every half a second."""
    #Note: Next we plan to add a check whether the AI and player have touched.
    #If not, continue. If yes, put up a game over screen
    angleDeg = calcAngle()
    if angleDeg==360:
        moveUpAI()
    elif angleDeg<360 and angleDeg<90:
        moveLeftAI()
        moveUpAI()
    elif angleDeg==90:
        moveLeftAI()
    elif angleDeg>90 and angleDeg<180:
        moveLeftAI()
        moveDownAI()
    elif angleDeg==180:
        moveDownAI()
    elif angleDeg>180 and angleDeg<270:
        moveDownAI()
        moveRightAI()
    elif angleDeg==270:
        moveRightAI()
    else:
        moveRightAI()
        moveUpAI()
    root.after(500,ai)
root.after(500,ai)
root.mainloop()

#This loop uses tkinter's after method - it calls a function after a specified
#amount of time has passed(in this case, it takes half a second to call the AI main function).
#As you can see, the same line that calls the function is in the function itself, essentially
#creating a while loop.
#We tried this with a normal while loop, but it conflicted with the main loop and crashed Python.
