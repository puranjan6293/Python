#Itretive method
"""
def factorial(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac

number=int(input("Enter question\n"))
print(factorial(number))

"""
#recursion method
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)
number=int(input("Enter your no-\n"))
print(factorial(number))