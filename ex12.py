class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __add__(self,point):
        return Point(self.x+point.x,self.y+point.y)

    def __str__(self):
        return "({0},{1})".format(self.x,self.y)


print("Poliformismo é quando o classes diferentes podem implementar diferentemente métodos de mesmo nome")
print("Duck Typing é quando a linguagem executa um método particular de um objeto, independente da sua classe")
print("Podemos usar a operação de soma como exemplo: 3 + 5 = ",3+5)

a = Point(1,2)
b = Point(2,4)

print("Para a classe Point, seria (1,2) + (2,4) = ", a + b)