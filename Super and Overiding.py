#OVERIDING


class A:
    classvar1="I am a class variable in class A"
    def __init__(self):#constructor
        self.classvar1= "I am inside A's Constructor"
        #Now adding a instance here
        self.classvar1="Instance var in class A" #pehle woh instance var ko hi print karega
        self.special = "Special"

class B(A):
    classvar2="I am a class variable in class B"
    def __init__(self):
        super().__init__() #used superconstructor
        self.classvar2= "I am inside B's constructor"


#instances

a=A()
b=B()

print(b.classvar2)
print(a.classvar1)
"""Outputs- I am inside B's constructor
I am inside A's Constructor"""

#After adding a instance variable the output is
"""I am inside B's constructor
Instance var in class A"""

print(b.special)
""" after that the output is - I am inside B's constructor
Instance var in class A
Special"""

"""
FROM HARRY SIR
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)

"""