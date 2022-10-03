#OPERATOR OVERLOADING AND DUNDER METHOD IN PYTHON

class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other): #dunder add method, it overloading the operator
        return self.salary+other.salary
    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee ('{self.name}',{self.salary},'{self.role}')"

    def __str__(self): #it will run 1st
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"



emp1=Employee("Harry",45000,"programmer") #ctrl+d for replicating this line
emp2=Employee("Rohan",5000,"cleaner")

print(emp1+emp2)
#output - 50000

print(emp1/emp2)
#output- 9.0

print(emp1)
#output is- <__main__.Employee object at 0x000002615E473E80>
#After def repr the output is- The Name is Harry. Salary is 45000 and role is programmer
#After changing the return function the output is- Employee ('Harry',45000,'programmer')

#After using the str function the output is- The Name is Harry. Salary is 45000 and role is programmer


