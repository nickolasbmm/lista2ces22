class Point:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x,self.y)

    def get_line_to(self,point):
        a = (point.y - self.y) / (point.x - self.x)
        b = (self.y * point.x - point.y * self.x)/(point.x - self.x)
        return (am,b)


print(Point(4,11).get_line_to(Point(6,15)))