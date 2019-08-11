class Giraffes:
    def left_forward(self):
        print('left foot forward')

    def left_backward(self):
        print('left foot backward')

    def right_forward(self):
        print('right foot forward')

    def right_backward(self):
        print('right foot backward')

    def dance(self):
        self.left_forward()
        self.left_backward()
        self.right_forward()
        self.right_backward()

a=Giraffes()
a.dance()