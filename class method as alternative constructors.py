#Class methods in python
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




harry = Employee("Harry", 255, "Instructor")
rohan= Employee("Harry", 455, "Student")
karan= Employee.from_dash("Karan-480-teacher")

karan.change_leaves(34)
print(karan.no_of_leaves)

print(karan.salary)