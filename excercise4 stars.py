"""
# Yasir Mehmood

print("How Many Row You Want To Print")
one= int(input())
print("Type 1 Or 0")
two = int(input())
new =bool(two)
if new == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new ==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*", end="")
        print()


#by my own
print("lets play a some game")
n1=int(input("Guess any number\n"))
n2=int(input("Chose Between 1 or 0\n"))
if n2==1:
    for item in range(0,n1+1):
        print(item*"*",end="\n")
elif n2==0:
    for meti in range(n1,0,-1):
        print(meti*"*",end="\n")


#My favoraite

print("Lets make a tringle")
n1=int(input("enter your choice\n"))
n2=int(input("chose 1 or 0\n"))
for i in range(n1):
    if n2==1:
        for j in range(i+1):
            print("*",end="")
        print()
    if n2==0:
        for j in range(i,n1):
            print("*",end="")
        print()
"""
#lets make a equal line tringle
print("Lets make a equal line tringle")
n1=int(input("enter how big you want to make\n"))
for i in range(n1):

    for j in range(i,n1):
        print(" ",end="")

    for j in range(i):
        print("*",end="")

    for j in range(i+1):
        print("*",end="")

    print()






