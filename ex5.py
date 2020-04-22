class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x,self.y)

    def reflect_x(self):
        return Point(self.x,-self.y)


p = Point(3,5)
print(p.reflect_x())