#Static method

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod   #Used for changing accessing by instance or class(simply hum ise harry se bhi chne kar sakte hne aur employe se bhi)
    def change_leaves(cls, newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):

        return cls(*string.split("-")) #oneliner

        # param=string.split("-")
        # print(param)
        # return cls(param[0],param[1],param[2])
    @staticmethod
    def printgood(string):
        print(" this is good " + string)
        return " Nice "

class Player:
    no_of_game=5
    def __init__(self, name, game):
        self.name=name
        self.game=game
    def printdetails(self):
        return f"the name is {self.name}. the game is {self.game}"

class CoolProgrammer(Employee,Player): #CLASS ORDER IS IMPORTANT
    languages="C++"
    def printlanguages(self):
        return f"the language is {self.languages}"

harry = Employee("Harry", 255, "Instructor")
rohan= Employee("Harry", 455, "Student")

karan=CoolProgrammer("Karan",45000,"coolprogrammer")

subham= Player("Subham", "BGMI")

#NOW ALL SET. LETS CHECK

print(karan.printdetails())
print(subham.printdetails())
print(subham.game)

print(karan.languages)

"""
#FROM SIR

class Employee:
    no_of_leaves = 8
    var = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

class Player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game =game

    def printdetails(self):
        return f"The Name is {self.name}. Game is {self.game}"

class CoolProgramer(Player, Employee):

    language = "C++"
    def printlanguage(self):
        print(self.language)

harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "Student")

shubham = Player("Shubham", ["Cricket"])
karan = CoolProgramer("Karan",["Cricket"])
# det = karan.printdetails()
# karan.printlanguage()
# print(det)
print(karan.var)

"""