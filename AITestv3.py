#imported functions

import sys
from tkinter  import *
from math import atan2,pi

#creation of windows,labels and canvas

window = Tk()
window.title('PAC-MAN')
mlabel=Label(text='PAC-MAN',fg='yellow',bg='blue').pack()
canvas = Canvas(window, width=500, height=500, bg = "white")
id1=canvas.create_rectangle(120,120,100, 100)
recAI=canvas.create_rectangle(380,380,400,400, fill = "black")
y_min = 0
y_max = 500
x_min = 0
x_max = 500

#movement code

vx = 10
vy = 10
v1x = 20
v1y = 20
def Left(event):
    x1,y1,x2,y2=canvas.coords(id1)
    if x1 == x_min :
        print("You're at the edge!")
        pass
    else:
        canvas.coords(id1,x1-vx,y1,x2-vx,y2)
def Right(event):
    x1,y1,x2,y2=canvas.coords(id1)
    if x2 == x_max:
        print("You're at the edge!")
        pass
    else:
        canvas.coords(id1,x1+vx,y1,x2+vx,y2)
def Down(event):
    x1,y1,x2,y2=canvas.coords(id1)
    if y2 == y_max:
        print("You're at the edge!")
        pass
    else:
        canvas.coords(id1,x1,y1+vy,x2,y2+vy)
def Up(event):
    x1,y1,x2,y2=canvas.coords(id1)
    if y1 == y_min:
        print("You're at the edge!")
        pass
    else:
        canvas.coords(id1,x1,y1-vy,x2,y2-vy)
canvas.bind('<Left>',Left)
canvas.bind('<Right>',Right)
canvas.bind('<Down>',Down)
canvas.bind('<Up>',Up)
canvas.focus_set()
canvas.pack(padx=10,pady=10)

#to here

#Teodor's AI code:

def calcAngle():
    x1,y1,x2,y2 = canvas.coords(id1)
    x3,y3,x4,y4 = canvas.coords(recAI)
    dx = x1-x3
    dy = y1-y3
    float(dx)
    float(dy)
    degrees = atan2(dx,dy)*(180/pi)
    degrees360 = degrees+180
    return degrees360
def moveUpAI():
    x3,y3,x4,y4 = canvas.coords(recAI)
    canvas.coords(recAI,x3,y3-v1y,x4,y4-v1y)
def moveDownAI():
    x3,y3,x4,y4 = canvas.coords(recAI)
    canvas.coords(recAI,x3,y3+v1y,x4,y4+v1y)
def moveLeftAI():
    x3,y3,x4,y4 = canvas.coords(recAI)
    canvas.coords(recAI,x3-v1x,y3,x4-v1x,y4)
def moveRightAI():
    x3,y3,x4,y4 = canvas.coords(recAI)
    canvas.coords(recAI,x3+v1x,y3,x4+v1x,y4)
def ai():
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
    canvas.after(300,ai)
canvas.after(300,ai)
canvas.mainloop()
