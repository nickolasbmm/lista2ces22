import abc

class Student:

    college = "ITA"

    def __init__(self,name,course):
        self.name = name
        self.course = course


    @classmethod
    def print_college_name(cls):
        print(cls.college)

    @staticmethod
    def print_average(scores):
        return print("Average = ",sum(scores)/len(scores))

    @abc.abstractmethod
    def designated_activity(self):
        raise NotImplementedError

class ReportCard(Student):

    def __init__(self,name,course,scores):
        super().__init__(name,course)
        self.scores = scores

    def designated_activity(self):
        self.print_average(self.scores)

class MedicalReport(Student):
    def __init__(self,name,course,condition):
        super().__init__(name,course)
        self.condition = condition

print("Cada tipo de método melhora o ambiente de produção do código:")
print("Métodos de classe são importantes para que nenhum desenvolvedor mude propriedades das intâncias por engano")
print("Métodos estáticos são importantes para que os métodos não sejam utilizados por outras classes de forma errada")
print("Métodos abstratos são importantes para que cada subclasse execute todos as atividades previstas para ela",end="\n\n")


print("Métodos de classe são métodos que só podem acessar propriedades da classe e não podem acessas propriedades de cada instância")

s = Student("nickolas","comp")
s.print_college_name()
Student.print_college_name()

print("Nesse caso o método print_college_name pode ser acessada mesmo sem existir uma instância da classe",end="\n\n")

print("Métodos estáticos não podem acessar nenhuma propriedade da classe nem das instâncias, são como funções comuns mas apenas para o sub-espaço da classe")
Student.print_average([65,75,90,100,80])
print("Veja que o método print_average só utilizada o parametro passado e nada mais",end="\n\n")

print("Métodos abstratos são métodos que são previstos para cada subclasse, mas que devem ser implementados independentemente")
print("Na classe ReportCard, o método designated_activity foi implementado e funciona corretamente")
r = ReportCard("nickolas","comp",[65,75,90,100,80])
r.designated_activity()
print("Na classe MedicalReport, o método não foi implementado, mostrando um erro")
m = MedicalReport("nickolas","comp","Healty")
m.designated_activity()