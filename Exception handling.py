"""
num1=input("Enter your first choice\n")
num2=input("Enter your second choice\n")
try:
    print("The sum is",int(num1)+int(num2))
except Exception as e:
    print(e)

print("This was done by prince p mallik")

#example
3
Enter your second choice
e
invalid literal for int() with base 10: 'e'
This was done by prince p mallik

#if we add here one number and one string than its not showing the error
#it print the last print function with the error

"""
