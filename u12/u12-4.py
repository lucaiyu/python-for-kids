from tkinter import*
import random
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
def random_rectangle(width,height,fill_color):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=random.randrange(width)
    y2=random.randrange(height)
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)

random_rectangle(400,400,'green')
