#Simple one
"""
print("Enter your age")
n1=18
n2=int(input())
if n2<n1:
    print("Sorry You Cannot drive")
elif n2==n1:
    print("Your age is 18,So we cann\'t decide")
if n2 > n1:
    print("Congratulations Sir You can drive")
else:
    print("Thanks For Using Our serviece Sir")
"""
#Lets do the Hardest one

print("Enter your age")
n1=7
n2=18
n3=100
n4=int(input())
if n4<n1:
    print("You are ineligible for Drive\n Go and Study")
elif n4==n1:
    print("You are ineligible sir\n Tum se na ho payega")
elif n4>n1 and n4<n2:
    print("sorry you can\'t drive\n go and play games")
elif n4>n2 and n4<n3:
    print("Congratulatins sir, You can drive\n Lets go for a long drive")
elif n4==n2:
    print("Sir you are eligible for Driving\n Go to the RTO and apply for your Driving licence ")
else:
    print("Pehli fursat me nikal bsdk")