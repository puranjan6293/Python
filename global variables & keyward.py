#Scope, Global & local variables
"""
#case1
l=10 #Global
def function1(n):
    l=5
    m=8
    print(l,m)
    print(n,"I have printed")
function1("this is me")
#output is
5 8 #here only value of l is printed 5, because here local variable l is given
#if l is note given than we will se in case2
this is me I have printed



# Case2
l=10 #Global
def function1(n):
    m=8
    print(l,m)
    print(n,"I have printed")
function1("this is me")

#output is
10 8 #here 10 is printed because we can use the global variable when local variable is not given
this is me I have printed


#case3
#can we increment the global variable inside local variable

l=10
def function1(n):
    m=8 #local variable
    global l #increment by using this first
    l=l+100
    print(l,m)
    print(n,"I have printed")
function1("This is me")

#output is
110 8
This is me I have printed

"""
