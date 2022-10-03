#Lambda functions or Anonymous
#Used for only convinious
#Without using lambda function
"""
a=int(input("a value\n"))
b=int(input("b value\n"))
def add(a,b):
    return a+b
print(add(a,b))


#By using lambda function

a=int(input("a value\n"))
b=int(input("b value\n"))

minus=lambda a,b:a-b
print(a-b)



# use of lambda with short function
#this is the normal one
def a_first(a):
    return a[1]

a=[[4,34],[6,3],[23,2],[34,12]]
a.sort(key=a_first)
print(a)
# output is
# [[23, 2], [6, 3], [34, 12], [4, 34]]

"""
#Lets use lambda function

a=[[4,34],[6,3],[23,2],[34,12]]
a.sort(key= lambda x:x[1]) #koi bhi function usko diya jaye to uska second element return kar de
print(a)

#output is same
# [[23, 2], [6, 3], [34, 12], [4, 34]]