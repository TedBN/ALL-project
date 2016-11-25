from tkinter import *
mGui = Tk()

mGui.geometry('450x450+50+50')
mGui.title('Pac man')

#canvas

canvas_1 = Canvas(mGui,height=300,width=300,bg ="white")
recPlayer = canvas_1.create_rectangle(13,13,28,28)
 
canvas_1.create_line(220,120,220,30)
canvas_1.create_line(200,100,180,100)
canvas_1.create_line(180,50,180,100)

canvas_1.create_rectangle(260,30,240,80, fill = "black")
#top right rectagle

canvas_1.create_line(220,30,160,30)
canvas_1.create_line(160,30,160,120)
canvas_1.create_line(220,120,240,120)
canvas_1.create_line(240,120,240,100)
canvas_1.create_line(220,100,240,100)


canvas_1.create_rectangle(240,100,220,120,fill = "black")
#right middle small square

canvas_1.create_line(260,140,260,80)
canvas_1.create_line(260,80,240,80)
canvas_1.create_line(240,30,260,30)

canvas_1.create_rectangle(200,50,180,100,fill = "black")
#middle top thin rectangle

canvas_1.create_line(260,30,260,100)
canvas_1.create_line(140,10,280,10)
canvas_1.create_line(280,160,280,10)
canvas_1.create_line(140,10,80,10)

canvas_1.create_rectangle(100,30,140,120, fill = "black")
#big rectangle to the right of the middle

canvas_1.create_line(160,120,180,120)
canvas_1.create_line(180,120,180,160)
canvas_1.create_line(200,140,200,120)
canvas_1.create_line(200,140,260,140)
canvas_1.create_line(160,140,30,140)

canvas_1.create_line(140,10,10,10)#line on the top
canvas_1.create_line(180,160,280,160)

canvas_1.create_line(10,10,10,240)#line on the right
canvas_1.create_line(30,30,30,120)

canvas_1.create_rectangle(80,30,50,120,fill = "black")

canvas_1.create_rectangle(280,160,240,200, fill = "black")
#right middle down square

canvas_1.create_line(280,200,280,280)
canvas_1.create_line(260,220,260,260)
canvas_1.create_line(260,220,220,220)
canvas_1.create_line(220,220,220,180)
canvas_1.create_line(220,180,160,180)
canvas_1.create_line(160,180,160,160)

canvas_1.create_rectangle(80,160,50,180,fill = "black")
#small black square on the left hand side of the middle

canvas_1.create_line(30,140,30,200)
canvas_1.create_line(30,200,60,200)
canvas_1.create_rectangle(10,280,60,240,fill = "black")
#bottom right square

canvas_1.create_rectangle(30,240,60,220,fill = "black")
#small box above bottom right square

canvas_1.create_line(80,200,80,260)
canvas_1.create_line(10,280,280,280)
canvas_1.create_line(80,200,100,200)
canvas_1.create_line(100,200,100,160)
canvas_1.create_line(100,160,140,160)
canvas_1.create_line(80,260,200,260)

canvas_1.create_rectangle(220,260,260,220, fill = "black")
#most bottom right square

canvas_1.create_line(200,260,200,200)
canvas_1.create_line(180,200,140,200)

canvas_1.create_rectangle(140,200,120,180,fill="black")
#left of middle small square

canvas_1.create_rectangle(100,240,180,220, fill = "black")
#bottom rectangle

canvas_1.pack()

vx = 10
vy = 10
def moveUp(event):
    """This function moves the player up"""
    x1,y1,x2,y2 = canvas_1.coords(recPlayer)
    Areax1 = x1
    Areay1 = y1-vy
    Areax2 = x2
    Areay2 = y2-vy
    object = canvas_1.find_overlapping(Areax1,Areay1,Areax2,Areay2)
    raw = 0
    firstCalc = True
    for x in object:
        if firstCalc == True:
            items = raw+(x-(x-1))
            firstCalc = False
        else:
            items = items+(x-(x-1))
    if items == 1:
        canvas_1.coords(recPlayer,x1,y1-vy,x2,y2-vy)
    else:
        print("There's an object in the way!")
    print(object)
    print(items)
def moveDown(event):
    """This function moves the player down"""
    x1,y1,x2,y2 = canvas_1.coords(recPlayer)
    Areax1 = x1
    Areay1 = y1+vy
    Areax2 = x2
    Areay2 = y2+vy
    object = canvas_1.find_overlapping(Areax1,Areay1,Areax2,Areay2)
    raw = 0
    firstCalc = True
    for x in object:
        if firstCalc == True:
            items = raw+(x-(x-1))
            firstCalc = False
        else:
            items = items+(x-(x-1))
    if items == 1:
        canvas_1.coords(recPlayer,x1,y1+vy,x2,y2+vy)
    else:
        print("There's an object in the way!")
    print(object)
    print(items)
def moveLeft(event):
    """This function moves the player left"""
    x1,y1,x2,y2 = canvas_1.coords(recPlayer)
    Areax1 = x1-vx
    Areay1 = y1
    Areax2 = x2-vx
    Areay2 = y2
    object = canvas_1.find_overlapping(Areax1,Areay1,Areax2,Areay2)
    raw = 0
    firstCalc = True
    for x in object:
        if firstCalc == True:
            items = raw+(x-(x-1))
            firstCalc = False
        else:
            items = items+(x-(x-1))
    if items == 1:
        canvas_1.coords(recPlayer,x1-vx,y1,x2-vx,y2)
    else:
        print("There's an object in the way!")
    print(object)
    print(items)
def moveRight(event):
    """This function moves the player right"""
    x1,y1,x2,y2 = canvas_1.coords(recPlayer)
    Areax1 = x1+vx
    Areay1 = y1
    Areax2 = x2+vx
    Areay2 = y2
    object = canvas_1.find_overlapping(Areax1,Areay1,Areax2,Areay2)
    raw = 0
    firstCalc = True
    for x in object:
        if firstCalc == True:
            items = raw+(x-(x-1))
            firstCalc = False
        else:
            items = items+(x-(x-1))
    if items == 1:
        canvas_1.coords(recPlayer,x1+vx,y1,x2+vx,y2)
    else:
        print("There's an object in the way!")
    print(items)
def coordCheck(event):
    """This function returns the player's current position on the canvas.
    It is called by left clicking on the canvas."""
    #Note: Used for debugging and will be removed in future.
    x1,y1,x2,y2 = canvas_1.coords(recPlayer)
    print(x1,y1)
canvas_1.focus_set()
canvas_1.bind("<Up>",moveUp)
canvas_1.bind("<Down>",moveDown)
canvas_1.bind("<Left>",moveLeft)
canvas_1.bind("<Right>",moveRight)
canvas_1.bind("<Button-1>",coordCheck)
canvas_1.pack()
mGui.mainloop()
