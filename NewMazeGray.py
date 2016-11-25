#New maze to be used in master file.

#TKinter is imported.
from tkinter import *

#Canvas is created and named.
root = Tk()
root.title("Steve-Man (Prototype ver.)")
maze = Canvas(root,width = 1125,height = 620,bg = "gray")

#This is a debug function that will be used to speed up
#the maze's construction.
def coordCheck(event):
    """This function returns the cursor's coordinates on the canvas.
    It is called by left clicking."""
    x = event.x
    y = event.y
    print(x,y)
maze.focus_set()
maze.bind("<Button-1>",coordCheck)

#Now the maze will be drawn.

#Top borders and pillars of the maze.
maze.create_line(25,25,1100,25, fill = "black")
maze.create_line(37,37,295,37,fill = "black")
maze.create_line(295,37,295,153,fill = "black")
maze.create_line(295,153,315,153,fill = "black")
maze.create_line(315,153,315,37,fill = "black")
maze.create_line(315,37,802,37,fill = "black")
maze.create_line(802,37,802,153,fill = "black")
maze.create_line(802,153,822,153,fill = "black")
maze.create_line(822,153,822,37,fill = "black")
maze.create_line(822,37,1082,37,fill = "black")

#Right borders of the maze.
maze.create_line(1100,25,1100,595,fill = "black")
maze.create_line(1082,37,1082,583,fill = "black")

#Bottom borders and pillars of the maze.
maze.create_line(1100,595,25,595,fill = "black")
maze.create_line(1082,583,822,583,fill = "black")
maze.create_line(822,583,822,468,fill = "black")
maze.create_line(822,468,801,468,fill = "black")
maze.create_line(801,468,801,583,fill = "black")
maze.create_line(801,583,315,583,fill = "black")
maze.create_line(315,583,315,468,fill = "black")
maze.create_line(315,468,295,468,fill = "black")
maze.create_line(295,468,295,583,fill = "black")
maze.create_line(295,583,37,583,fill = "black")

#Left borders of the maze.
maze.create_line(25,595,25,25,fill = "black")
maze.create_line(37,583,37,37, fill = "black")

#Objects on the left side of the maze(from top to bottom).

#Triangular shapes.
maze.create_line(109,132,219,132,fill = "black")
maze.create_line(109,132,109,262,fill = "black")
maze.create_line(109,262,129,262,fill = "black")
maze.create_line(129,262,129,152,fill = "black")
maze.create_line(129,152,219,152,fill = "black")
maze.create_line(219,152,219,132,fill = "black")
maze.create_line(109,488,219,488,fill = "black")
maze.create_line(109,488,109,358,fill = "black")
maze.create_line(109,358,129,358,fill = "black")
maze.create_line(129,358,129,468,fill = "black")
maze.create_line(129,468,219,468,fill = "black")
maze.create_line(219,468,219,488,fill = "black")

#Rectangles.
maze.create_line(315,262,260,262,fill = "black")
maze.create_line(260,262,260,247,fill = "black")
maze.create_line(260,247,315,247,fill = "black")
maze.create_line(315,247,315,262,fill = "black")
maze.create_line(315,358,260,358,fill = "black")
maze.create_line(260,358,260,373,fill = "black")
maze.create_line(260,373,315,373,fill = "black")
maze.create_line(315,373,315,358,fill = "black")

#Objects on the right side of the maze(from top to bottom).

#Triangular shapes.
maze.create_line(898,133,1008,133,fill = "black")
maze.create_line(1008,133,1008,266,fill = "black")
maze.create_line(1008,266,988,266,fill = "black")
maze.create_line(988,266,988,153,fill = "black")
maze.create_line(988,153,898,153,fill = "black")
maze.create_line(898,153,898,133,fill = "black")
maze.create_line(898,488,1008,488,fill = "black")
maze.create_line(1008,488,1008,355,fill = "black")
maze.create_line(898,488,898,468,fill = "black")
maze.create_line(898,468,988,468,fill = "black")
maze.create_line(988,468,988,355,fill = "black")
maze.create_line(988,355,1008,355,fill = "black")

#Rectangles.
maze.create_line(802,263,857,263,fill = "black")
maze.create_line(857,263,857,248,fill = "black")
maze.create_line(857,248,802,248,fill = "black")
maze.create_line(802,248,802,263,fill = "black")
maze.create_line(802,358,857,358,fill = "black")
maze.create_line(857,358,857,373,fill = "black")
maze.create_line(857,373,802,373,fill = "black")
maze.create_line(802,373,802,358,fill = "black")

#Objects in the middle.

#Walls(first is top, second is bottom).
maze.create_line(404,153,714,153,fill = "black")
maze.create_line(404,153,404,133,fill = "black")
maze.create_line(714,153,714,133,fill = "black")
maze.create_line(714,133,404,133,fill = "black")
maze.create_line(714,468,404,468,fill = "black")
maze.create_line(404,468,404,488,fill = "black")
maze.create_line(714,468,714,488,fill = "black")
maze.create_line(714,488,404,488,fill = "black")

#Middle rectangle.
maze.create_line(404,247,404,373,fill = "black")
maze.create_line(404,373,714,373,fill = "black")
maze.create_line(714,373,714,247,fill = "black")
maze.create_line(714,247,634,247,fill = "black")
maze.create_line(404,247,484,247,fill = "black")
maze.create_line(484,247,484,267,fill = "black")
maze.create_line(634,247,634,267,fill = "black")
maze.create_line(484,267,424,267,fill = "black")
maze.create_line(634,267,694,267,fill = "black")
maze.create_line(694,267,694,353,fill = "black")
maze.create_line(694,353,424,353,fill = "black")
maze.create_line(424,353,424,267,fill = "black")

#Note:I know that there is a create_rec tangle method,
#but if I use it it will colour the entire rectangle
#blue instead of just the lines forming them.

#The maze is packed and ready to go!
maze.pack(padx = 10,pady = 10)
root.mainloop()
