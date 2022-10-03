# Public -
# Protected -
# Private -

class Employee:
    no_of_leaves = 8 #public
    var = 8 #public
    _protect=9 #protected started from underscore
    __private=90 #private started from double underscore

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

emp=Employee("Harry",34000,"cricketer")

print(emp._protect) #using this for accessing protected functions
print(emp._Employee__private) #using this for accessing private function
#called name mengling