#The following code is the original design for the start Menu
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import filedialog

def mNew():
    mlabel3 = label(mGui,text="You clicked New").pack()
    return

def mAbout():
    messagebox.showinfo(title = "About",message="This is a first year project for computer sciencer students from Coventry Uni. The game is made in python3 ")
    return

def mQuit():
    mExit = messagebox.askokcancel(title="Quit",message = "Do You Wish to Quit?")
    if mExit > 0 :
        mGui.destroy()
        return

def mColour():
    mycolour = colorchooser.askcolor()
    mlabel4 = label(mGui,text=mycolour).pack()
    return

def mOpen():
    myopen = filedialog.askopenfile()
    label5 = label(mGui,text = myopen).pack()
    return

                                           
mGui = Tk()
ment = StringVar()

mGui.geometry('450x450+500+300')
#This will create a tab of the following size
mGui.title('Pac-Man')

mLabel = Label(text = 'PAC - MANIA',fg = 'yellow',bg = 'blue',).pack()


mButton = Button(mGui,text = 'START',bg = 'yellow')
mButton.pack()
mButton.bind("<Enter>", lambda event, h=mButton: h.configure(bg="red"))
mButton.bind("<Leave>",lambda event, h=mButton: h.configure(bg="yellow"))
#The lines above will change the colour of the start button when the cursor
#hovers over it

#mGui.mainloop()

menubar =Menu(mGui)

filemenu = Menu(menubar)
filemenu.add_command(label = "New",command = mNew)
filemenu.add_command(label = "Open", command = mOpen)
filemenu.add_command(label = "Save As...")
filemenu.add_command(label = "Close",command = mQuit)
filemenu.add_command(label = "Colour",command = mColour)

menubar.add_cascade(label = "File",menu=filemenu)

mGui.config(menu=menubar)
#The above sectrion oif code wilol create a menu oin the top left of the screen


helpmenu = Menu(menubar,tearoff = 0)
helpmenu.add_command(label = "Help Docs")
helpmenu.add_command(label = "About", command = mAbout)
menubar.add_cascade(label = "Help",menu=helpmenu)

mGui.config(menu=menubar)


