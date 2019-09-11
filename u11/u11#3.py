import turtle
t=turtle.Pen()
def draw_star(size,pionts1,pionts2):
    for x in range(0,pionts1):
        t.forward(size)
        t.left(pionts2)

