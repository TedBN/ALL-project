#imported functions

import sys
from tkinter  import *
from math import atan2,pi
import tkinter as tk

#creation of windows,labels and canvas
#Deyan Bozhilov imported sprites
#the player and the AI now have assigned sprites
#Teodor Atanasov contributed to the import of the sprites

window = Tk()
window.title('PAC-MAN')
mlabel=Label(text='PAC-MAN',fg='yellow',bg='blue').pack()

canvas = Canvas(window, width=500, height=500, bg = "white")

#sprite number 1 is the player
gif1 = PhotoImage(file = 'piskel.gif')
id1=canvas.create_image(120,100,image=gif1) 
#AI-1
gif2 = PhotoImage(file = 'enemy1.gif')
recAI=canvas.create_image(380,400,image = gif2)
#AI-2
gif3= PhotoImage(file = 'enemy2.gif')
recAI2=canvas.create_image(430,450,image = gif3)
#AI-3
gif4= PhotoImage(file = 'enemy3.gif')
recAI3=canvas.create_image(280,300,image = gif4)

#movement code
#colaboration between Teodor Atanasov and Deyan Bozhilov
#borders to the window removed due to optimization to the maze

#speed values of the player
vx = 10
vy = 10

#speed values of the AI
v1x = 10
v1y = 10

def Left(event):
    x1,y1=canvas.coords(id1)
    canvas.coords(id1,x1-vx,y1)
def Right(event):
    x1,y1=canvas.coords(id1)
    canvas.coords(id1,x1+vx,y1)
def Down(event):
    x1,y1=canvas.coords(id1)
    canvas.coords(id1,x1,y1+vy)
def Up(event):
    x1,y1=canvas.coords(id1)
    canvas.coords(id1,x1,y1-vy)

canvas.bind('<Left>',Left)
canvas.bind('<Right>',Right)
canvas.bind('<Down>',Down)
canvas.bind('<Up>',Up)
canvas.focus_set()

canvas.pack(padx=10,pady=10)

#to here

#Teodor's AI code:
#Deyan added 2 new variables and 2 new canvas objects:

def calcAngle(AIobj):
    x1,y1 = canvas.coords(id1)
    x2,y2 = canvas.coords(AIobj)   
    dx = x1-x2
    dy = y1-y2
    float(dx)
    float(dy)
    degrees = atan2(dx,dy)*(180/pi)
    degrees360 = degrees+180
    return degrees360
def moveUpAI(obj):
    x1,y1 = canvas.coords(obj)
    canvas.coords(obj,x1,y1-v1y)
def moveDownAI(obj):
    x1,y1 = canvas.coords(obj)
    canvas.coords(obj,x1,y1+v1y)
def moveLeftAI(obj):
    x1,y1 = canvas.coords(obj)
    canvas.coords(obj,x1-v1x,y1)
def moveRightAI(obj):
    x1,y1 = canvas.coords(obj)
    canvas.coords(obj,x1+v1x,y1)
def aiAction(enemy):
    angleDeg = calcAngle(enemy)
    if angleDeg==360:
        moveUpAI(enemy)
    elif angleDeg<360 and angleDeg<90:
        moveLeftAI(enemy)
        moveUpAI(enemy)
    elif angleDeg==90:
        moveLeftAI(enemy)
    elif angleDeg>90 and angleDeg<180:
        moveLeftAI(enemy)
        moveDownAI(enemy)
    elif angleDeg==180:
        moveDownAI(enemy)
    elif angleDeg>180 and angleDeg<270:
        moveDownAI(enemy)
        moveRightAI(enemy)
    elif angleDeg==270:
        moveRightAI(enemy)
    else:
        moveRightAI(enemy)
        moveUpAI(enemy)
def ai():
    aiAction(recAI)
    aiAction(recAI2)
    aiAction(recAI3)
    canvas.after(300,ai)
canvas.after(300,ai)
canvas.mainloop()
