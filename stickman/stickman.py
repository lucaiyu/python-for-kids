#!/usr/bin/env python3

from tkinter import*
import random
import time

class Game:
    def __init__(self):
        self.tk=Tk()
        self.tk.title("Mr.Stick Man Races for the exit")
        self.tk.resizable(0,0)
        self.tk.wm_attributes("-topmost",1)
        self.canvas=Canvas(self.tk,width=500,height=500,highlightthickness=0)
        self.canvas.pack()
        self.tk.update()
        self.canvas_height=500
        self.canvas_width=500
        self.bg=PhotoImage(file="background.gif")
        w=self.bg.width()
        h=self.bg.height()
        for x in range(0,5):
            for y in range(0,5):
                self.canvas.create_image(x*w,y*h,image=self.bg,anchor='nw')

        self.sprites=[]
        self.running=True

    def mainloop(self):
        while True:
            if self.running==True:
                for sprite in self.sprites:
                    sprite.move()

            self.tk.update_idletasks()
            self.tk.update()
            time.sleep(0.05)

class Coords:
    def __init__(self,x1=0,y1=0,x2=0,y2=0):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

def within_x(co1,co2):
    if(co1.x1>co2.x1 and co1.x2<co2.x2) or (co1.x2>co2.x1 and co1.x2<co2.x2) or (co2.x1>co1.x1 and co2.x1<co1.x2) or (co2.x2>co1.x1 and co2.x2<co1.x1):
        return True
    else:
        return False

def within_y(co1,co2):
    if(co1.y1>co2.y1 and co1.y2<co2.y2) or (co1.y2>co2.y1 and co1.y2<co2.y2) or (co2.y2>co1.y1 and co2.y1<co1.y2) or (co2.y2>co1.y1 and co2.y2<co2.y1):
        return True
    else:
        return False

def collided_left(co1,co2):
    if within_y(co1,co2):
        if co1.x1<=co2.x2 and co1.x1>=co2.x1:
            return True

    return False

def collided_right(co1,co2):
    if within_y(co1,co2):
        if co1.x2>=co2.x1 and co1.x2<=co2.x2:
            return True

    return False

def collided_top(co1,co2):
    if within_x(co1,co2):
        if co1.y1<=co2.y2 and co1.y1>=co2.y1:
            return True

    return False

def collided_bottom(y,co1,co2):
    if within_x(co1,co2):
        y_calc=co1.y2+y
        if y_calc>=co2.y1 and y_calc<=co2.y2:
            return True

    return False

class Sprite:
    def __init__(self,game):
        self.game=game
        self.endgame=False
        self.coordinates=None

    def move(self):
        pass

    def coords(self):
        return self.coordinates

class p(Sprite):
    def __init__(self,game,photo_image,x,y,width,height):
        Sprite.__init__(self,game)
        self.photo_image=photo_image
        self.image=game.canvas.create_image(x,y,image=self.photo_image,anchor='nw')
        self.coordinates=Coords(x,y,x+width,y+height)

class StickFigureSprite(Sprite):
    def __init__(self,game):
        Sprite.__init__(self,game)
        self.images_left=[PhotoImage(file="stick-L1.gif"),PhotoImage(file="stick-L2.gif"),PhotoImage(file="stick-L3.gif")]
        self.images_right=[PhotoImage(file="stick-R1.gif"),PhotoImage(file="stick-R2.gif"),PhotoImage(file="stick-L3.gif")]
        self.image=game.canvas.create_image(200,470,image=self.images_left[0],anchor='nw')
        self.x=-2
        self.y=0
        self.current_image=0
        self.current_image_add=1
        self.jump_count=0
        self.last_time=time.time()
        self.coordinates=Coords()
        game.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        game.canvas.bind_all('<space>',self.jump)

    def turn_left(self,evt):
        self.x=-0.5

    def turn_right(self,evt):
        self.x=0.5

    def jump(self,evt):
        self.y=-0.5
        self.jump_count=0

    def animate(self):
        if self.x!=0 and self.y==0:
            if time.time()-self.last_time>0.1:
                self.last_time=time.time()
                self.current_image+=self.current_image_add
                if self.current_image>=2:
                    self.current_image_add=-1

                if self.current_image<=0:
                    self.current_image_add=1

                if self.x<0:
                    if self.y!=0:
                        self.game.canvas.itemconfig(self.image,image=self.images_left[2])

                    else:
                        self.game.canvas.itemconfig(self.image,image=self.images_left[self.current_image])

                elif self.x>0:
                    if self.y!=0:
                        self.canvas.itemconfig(self.image,image=self.images_right[2])

                    else:
                        self.game.canvas.itemconfig(self.image,image=self.images_right[self.current_image])

    def coords(self):
        xy=self.game.canvas.coords(self.image)
        self.coordinates.x1=xy[0]
        self.coordinates.y1=xy[1]
        self.coordinates.x2=xy[0]+50
        self.coordinates.y2=xy[1]+80
        return self.coordinates

    def move(self):
        self.animate()
        if self.y<0:
            self.jump_count+=1
            if self.jump_count>20:
                self.y=1

        if self.y>0:
            self.jump_count-=1

        co=self.coords()
        left=True
        right=True
        top=True
        bottom=True
        falling=True
        if self.y>0 and co.y2>self.game.canvas_height:
            self.y=0
            bottom=False

        if self.y<0 and co.y1<=0:
            self.y=0
            top=False

        if self.x>0 and co.x2>=self.game.canvas_width:
            self.x=0
            right=False

        if self.x<0 and co.x1<=0:
            self.x=0
            left=False

        for sprite in self.game.sprites:
            if sprite==self:
                continue

            sprite_co=sprite.coords()
            if top and self.y<0 and collided_top(co,sprite_co):
                self.y=-self.y
                top=False

            if bottom and self.y>0 and collided_bottom(self.y,co,sprite_co):
                self.y=sprite_co.y1-co.y2
                if self.y<0:
                    self.y=0

                bottom=False
                top=False

            if bottom and falling and self.y==0 and co.y2<self.game.canvas_height and collided_bottom(1,co,sprite_co):
                falling=False
                if left and self.x<0 and collided_left(co,sprite_co):
                    self.x=0
                    left=False
                    if sprite.endgame:
                        self.game.running=False

                if right and self.x>0 and collided_right(co,sprite_co):
                    self.x=0
                    right=False
                    if sprite.endgame:
                        self.game.running=False

            if falling and bottom and self.y==0 and co.y2< self.game.canvas_height:
                self.y=4

            self.game.canvas.move(self.image,self.x,self.y)

class DoorSprite(Sprite):
    def __init__(self,game,photo_image,x,y,width,height):
        Sprite.__init__(self,game)
        self.photo_image=photo_image
        self.image=game.canvas.create_image(x,y,image=self.photo_image,anchor='nw')
        self.coordinates=Coords(x,y,x+(width/2),y+height)
        self.endgame=False




g=Game()

sm=StickFigureSprite(g)
door=DoorSprite(g,PhotoImage(file="door.gif"),45,30,50,80)
p1=p(g,PhotoImage(file="1.gif"),0,480,100,10)
p2=p(g,PhotoImage(file="1.gif"),150,440,100,10)
p3=p(g,PhotoImage(file="1.gif"),300,400,100,10)
p4=p(g,PhotoImage(file="1.gif"),300,160,100,10)
p5=p(g,PhotoImage(file="2.gif"),175,350,90,10)
p6=p(g,PhotoImage(file="2.gif"),100,300,90,10)
p7=p(g,PhotoImage(file="2.gif"),170,120,90,10)
p8=p(g,PhotoImage(file="2.gif"),45,60,90,10)
p9=p(g,PhotoImage(file="3.gif"),170,250,80,10)
p10=p(g,PhotoImage(file="3.gif"),230,200,80,10)
g.sprites.append(p1)
g.sprites.append(p2)
g.sprites.append(p3)
g.sprites.append(p4)
g.sprites.append(p6)
g.sprites.append(p7)
g.sprites.append(p8)
g.sprites.append(p10)
g.sprites.append(sm)
g.sprites.append(door)
g.mainloop()
