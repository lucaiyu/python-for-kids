from tkinter import*
import random
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
image=PhotoImage(file='/home/aiyu/aiyupy/python-for-kids/a.gif')
canvas.create_image(0,0,anchor=NW,image=image)
