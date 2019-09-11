from tkinter import*
import random
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
canvas.create_arc(10,10,200,100,extent=180,style=ARC)
