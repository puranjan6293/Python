#Making an fibonachi sequence
"""
#using recursion method
def fibonachi(n):

    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonachi(n-1)+fibonachi(n-2)
number=int(input("Enter your question\n"))
print(fibonachi(number))

"""
#Using itretive method
i=0
a = 0
b = 1
n = int(input("Enter ant no\n"))
for i in range(n) :
    i = i+1
    c = a+b
    print(c, end=" ")
    a = b
    b = c





