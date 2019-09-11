from tkinter import*
import time
tk=Tk()
canvas=Canvas(tk,width=500,height=500)
canvas.pack()
image=PhotoImage(file='/home/aiyu/aiyupy/python-for-kids/a.gif')
canvas.create_image(0,0,anchor=NW,image=image)
for x in range(0,20):
    canvas.move(1,5,0)
    tk.update()
    time.sleep(0.05)
