class Shape:
    geometric_type = "Generic Shape"

    def area(self):
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:

    def plot(self,ratio,topleft):
        print ("Plotting at {}, ratio {}.".format(topleft,ratio))

class Polygon(Shape,Plotter):
    geometric_type = "Polygon"

class RegularPolygon(Polygon):
    geometric_type = "Regular Polygon"

    def __init__(self,side):
        self.side = side

class RegularHexagon(RegularPolygon):
    geometric_type = "Regular Hexagon"

    def area(self):
        return 1.5 * (3**0.5 * self.side**2)

class Square(RegularPolygon):
    geometric_type = "Square"

    def area(self):
        return self.side * self.side

print("Só existe um tipo de MRO em python, que começa pela classe, no caso Square, depois suas classes pais, na ordem em que elas foram escritas na criação da classe")
print("Por exemplo: a classe Polygon é subclasse de Shape e Plotter, nessa ordem, então no MRO Shape aparecerá antes de Plotter",end="\n\n")
print("MRO da classe Square:",Square.mro())