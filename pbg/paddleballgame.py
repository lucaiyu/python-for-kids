from tkinter import*
import random
import time
import sys
t1=time.time()
class Ball:
    def __init__(self,canvas,paddle,color):
        self.canvas=canvas
        self.paddle=paddle
        self.id=canvas.create_oval(10,10,20,20,fill=color)
        self.canvas.move(self.id,245,100)
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x=starts[0]
        self.y=-1
        self.num=0
        self.canvas_height=self.canvas.winfo_height()
        self.canvas_width=self.canvas.winfo_width()
        self.hit_bottom=False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2] and pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                return True

        return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[1]<=0:
            self.y=1

        if pos[3]>=self.canvas_height:
            self.hit_bottom=True

        if self.hit_paddle(pos)==True:
            self.y=-1
            self.num+=1

        if pos[0]<=0:
            self.x=1

        if pos[2]>=self.canvas_width:
            self.x=-1

class Paddle:
    def __init__(self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,75,5,fill=color)
        self.canvas.move(self.id,200,300)
        self.x=0
        self.y=0
        self.canvas_width=self.canvas.winfo_width()
        self.canvas_height=self.canvas.winfo_height()
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)
        self.canvas.bind_all('<space>',self.stop)


    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos=self.canvas.coords(self.id)
        if pos[0]<=0:
            self.x=0

        if pos[2]>=self.canvas_width:
            self.x=-0

        if pos[3]>=self.canvas_height:
            self.y=-0

        if pos[1]<=0:
            self.y=0

    def turn_left(self,evt):
        self.x=-3
        self.y=0


    def turn_right(self,evt):
        self.x=3
        self.y=0

    def turn_up(self,evt):
        self.y=-3
        self.x=0

    def turn_down(self,evt):
        self.y=3
        self.x=0

    def stop(self,evt):
        self.x=0
        self.y=0


tk=Tk()
tk.title('Paddleballgame')
tk.resizable(0,0)
tk.wm_attributes('-topmost',1)
canvas=Canvas(tk,width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()
paddle=Paddle(canvas,'blue')
ball1=Ball(canvas,paddle,'red')
print('Start Game!')
while True:
    if ball1.hit_bottom==False:
        ball1.draw()
        paddle.draw()

    else:
        t2=time.time()
        logtime=time.asctime()
        log='\n'+str(logtime)+'   '+str(ball1.num)+'   '+str(t2-t1)+'   False'+'\n'

        file=open('log.txt','a')
        file.write(log)
        file.close()
        a=PhotoImage(file='gameover.gif')
        canvas.create_image(0,0,anchor=NW,image=a)




    if ball1.num>=5:
        t2=time.time()
        logtime=time.asctime()
        log='\n'+str(logtime)+'   '+str(5)+'   '+str(t2-t1)+'   True'+'\n'

        file=open('log.txt','a')
        file.write(log)
        file.close()
        b=PhotoImage(file='win.gif')
        canvas.create_image(0,0,anchor=NW,image=b)






    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

