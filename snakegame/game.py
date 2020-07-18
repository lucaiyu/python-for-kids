from tkinter import*
from random import*
from time import*
from sys import*
tk=Tk()
tk.title('A snake want to eat all of the food,please help it.')
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas=Canvas(tk,width=600,height=600,highlightthickness=0)
canvas.pack()
tk.update()
bg=PhotoImage(file='background.gif')
w=200
h=200
for x in range(0,4):
    for y in range(0,4):
        canvas.create_image(x*w,y*h,image=bg,anchor='nw')

while True:
    tk.update_idletasks()
    tk.update()
    sleep(0.1)
