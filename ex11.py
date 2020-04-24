#Function with argument list
def square_sequence(*arglist):
    print("Squared sequence: ",end="")
    for x in arglist:
        print("{} ".format(x**2),end="")
    print("")
print("Example function with argument list")
print("Initial sequence: 1 2 3 4 5")
square_sequence(1,2,3,4,5)

#Functio with argument dictionary

def person_function(**argdict):
    for key in argdict:
        print(key," works as: ",argdict[key])

print("Example function with argument dictionary")
person_function(Anne = "Student", John = "Professor", Ralph = "Shopkeeper")