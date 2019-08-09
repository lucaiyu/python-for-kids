class Things:
    pass

class Inanimate(Things):
    pass

class Animate(Things):
    pass

class Sidewalks(Inanimate):
    pass

class Animals(Animate):
    def breathe(self):
        print('breathing')

    def move(self):
        print('moveing')

    def eat_food(self):
        print('eating')

class Mammals(Animals):
    def feed_young_with_milk(self):
        print('feeding')

class Giraffes(Mammals):
    def eat_leaves_from_trees(self):
        print('eating leaves' )


a=Giraffes()
b=Giraffes()

a.move()

b.eat_leaves_from_trees()



