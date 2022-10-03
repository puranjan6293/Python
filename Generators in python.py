#Generators in python

"""
iterable-
iterator-
iteration-



def gen(n):
    for i in range(n):
        yield i

g=gen(3000000)
print(g)

"""

#MAKING FIBONACHI SERIES AND FACTORIAL OF N

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# s=int(input())
# g=factorial(s)
# print(g)

def fibonachi(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        yield c
        a=b
        b=c
n=int(input("Enter your no\n"))
val=fibonachi(n)
for i in val:
    print(i)