import turtle
t=turtle.Pen()
def eight(filled,size):
    if filled==True:
        t.begin_fill()

    for x in range(0,8):
        t.forward(size)
        t.left(45)

    if filled==True:
        t.end_fill()