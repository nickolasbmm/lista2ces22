class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x,self.y)

    def slope_from_origin(self):
        if self.x==0:
            return "Error: can't divide by zero"
        return self.y/self.x


p = Point(4,10)
print(p.slope_from_origin())

#Error occurs at points on the y axis
print(Point(0,10).slope_from_origin())