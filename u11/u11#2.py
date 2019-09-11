import turtle
t=turtle.Pen()
def draw_star(size):
    for x in range(0,19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)

        else:
            t.left(225)