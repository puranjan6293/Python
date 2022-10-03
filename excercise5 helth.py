
print("Welcome to  Health Management System")

print("For which client Do you want to Log or retrieve")
print("Click :\n""1 for Harry\n""2 for Rohan\n""3 For Hammad\n")
n=int(input())
print("Press E for Exercise or F for Food")
b=input()
print("Press L for Log or R for Retrieve")
r=input()

def getdate():
    import datetime
    return datetime.datetime.now()

if n==1:
    if r == "L":
        if b == "E":
            print()
            print()
            print("Please enter what do you want to add")
            z = input()
            print("Successfully added!")
            with open("harry-ex.txt", "a") as op:
                time = str(getdate())
                op.write(z  + "[" + time + "]" + "\n")
if n==1:
    if r == "R":
        if b == "E":
            print()
            print()
            print()
            print("Here is your information!")
            f=open("harry-ex.txt","rt")
            content = f.read()
            print(content)
            f.close()

if r=="L":
    if b=="F":
        if n==1:
            print()
            print()
            print("Please enter what do you want to add")
            z1 = input()
            print("Successfully added!")
            with open("harry-fo.txt", "a") as op1:
                time = str(getdate())
                op.write(z1 + "[" + time + "]" + "\n")
if n==1:
    if r == "R":
        if b == "F":
            print()
            print()
            print()
            print("Here is your information!")
            f=open("harry-fo.txt","rt")
            content = f.read()
            print(content)
            f.close()

if n==2:
    if r == "L":
        if b=="E":
            print()
            print()
            print("Please enter what do you want to add")
            z2 = input()
            print("Successfully added!")
            with open("rohan-ex.txt", "a") as op:
                time = str(getdate())
                op.write(z2  +  "[" + time + "]" + "\n")
if n==2:
    if r == "R":
        if b == "E":
            print()
            print()
            print()
            print("Here is your information!")
            f=open("rohan-ex.txt","rt")
            content = f.read()
            print(content)
            f.close()
if n==2 and r=="L":
    if b=="F":
            print()
            print("Please enter what do you want to add")
            z3 = input()
            print("Successfully added!")
            with open("rohan-fo.txt", "a") as op:
                time = str(getdate())
                op.write(z3 + "[" + time + "]" + "\n")
if n==2:
    if r == "R":
        if b == "F":
            print()
            print()
            print()
            print("Here is your information!")
            f=open("rohan-fo.txt","rt")
            content = f.read()
            print(content)
            f.close()
if n==3:
    if r=="L":
        if b=="E":
            print()
            print()
            print("Please enter what do you want to add")
            z4=input()
            print("Successfully added!")
            with open("hammad-ex.txt", "a") as op:
                time = str(getdate())
                op.write(z4 + "[" + time + "]" + "\n")
if n==3:
    if r == "R":
        if b == "E":
            print()
            print()
            print()
            print("Here is your information!")
            f=open("hammad-ex.txt","rt")
            content = f.read()
            print(content)
            f.close()
if n==3:
    if r=="L":
        if b=="F":
            print()
            print()
            print("Please enter what do you want to add")
            z5=input()
            print("Successfully added!")
            with open("hammad-fo.txt", "a") as op:
                time = str(getdate())
                op.write(z5 + "[" + time + "]" + "\n")
if n==3:
    if r == "R":
        if b == "F":
            print()
            print()
            print()
            print("Here is your information!")
            f=open("hammad-fo.txt","rt")
            content = f.read()
            print(content)
            f.close()
