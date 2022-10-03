"""
#Builtin functions
a=9
b=8
c=sum((a,b)) #sum is builtin function
print(c)
#output is 17


#Functions that can made by us
def function1():
    print("you are in function1")
print(function1())

#output is
you are in function1
None #here none is came because we added a extra print function on last


#slight advance
def function1():
    print("You are in function1")
function1()
#output is You are in function1
#if we want multiple print than we have to add multiple function1 function on last
#example
function1()
function1()
function1()
#output is You are in function1
#You are in function1
#You are in function1
#You are in function1


#full advancement
#Function input bhi le sakt hai
#example
def function1(a,b):
    print("hello you are in function1",a+b)
#output is hello you are in function1 14

def function2(c,d):
    avarage=(c+d)/2
    print(avarage)
function2(9, 5)
#output is 7.0


#Use of return function
def function1(a,b):
    avarage=(a+b)/2
    #print(avarage)
    return (avarage)
v=function1(9,5)
print(v)

#output is 6.0
"""

#Docstring

def function1(a,b):
    """This is a function which will calculate the avarage of two numbers"""
    avarage=(a+b)/2
    #print(avarage)
    return (avarage)

print(function1.__doc__)
#output is - This is a function which will calculate the avarage of two numbers