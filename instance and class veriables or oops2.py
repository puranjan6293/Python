# instance and class veriables

class Employee:

    no_of_leaves=8
    pass

harry=Employee()
rohan=Employee()

harry.name="Harry"
harry.std=10
harry.group=3
harry.sal=1000

rohan.name="Rohan"
rohan.std=9
rohan.group=4
rohan.sal=4000
"""
print(harry.std)
print(Employee.no_of_leaves)
print(harry.no_of_leaves)
print(rohan.no_of_leaves)
"""
#the above three print statements outputs are same

#but if we want to change the no_of_leave than rohan and harry can't chane it
#only Employee can change it

Employee.no_of_leaves=20

print(harry.no_of_leaves)
print(rohan.no_of_leaves)
print(Employee.no_of_leaves)

#the above three print statements output is same that is changed
#output is 20

#from sir

class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)