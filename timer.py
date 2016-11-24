from tkinter import *

root = Tk()
root.title('Timer')

sec = 0

def timer():
    global sec #global allows me to use the variable sec inside a definition
    sec = sec + 1
    time['text'] = sec
    # the above line will display the time to the user
    time.after(1000, timer)

time = Label(root, fg='blue') #this is the label which outputs time to the user
time.pack()
Button(root, fg='blue', text='Start', command=timer).pack()
#the above line creates a button which the user will press to start the timer
root.mainloop()

#This program is a timer, which counts in seconds
#The program begins once the START button is pressed
