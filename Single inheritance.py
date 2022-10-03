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

#SINGLE INHERITANCE

class Programmer(Employee):
    no_of_hollydays=56
    #ADDING NEW LIST

    def __init__(self, aname, asalary, arole, languages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages


    def printprog(self):
        return f"The programmer's name is {self.name}. salary is {self.salary}. role is {self.role}. The languages are {self.languages}"


harry = Employee("Harry", 255, "Instructor")
rohan= Employee("Harry", 455, "Student")
karan= Employee.from_dash("Karan-480-teacher")
#     for programmer
subham=Programmer("Subham",999,"programmer",["python"])
shivam=Programmer("Sivam",777,"programmer",["python"])


# karan.change_leaves(34)
# print(karan.no_of_leaves)
#
# print(karan.printgood("harry"))

print(shivam.printprog())
#output is-The programmer's name is Sivam. salary is 777. role is programmer
print(subham.salary)
#output is 999
print(subham.no_of_hollydays)
#output is 56