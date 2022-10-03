#Map,Filters and reduce
"""
#Without using map function

numbers=["30","40","94"]
for i in range(len(numbers)):
    numbers[i]=int(numbers[i])

numbers[2]=numbers[2]+1
print(numbers[2])


#Now lets use map function
#example1
numbers=["30","40","94"]

numbers=list(map(int,numbers))

numbers[2]=numbers[2]+1
print(numbers[2])
#output - 95



#Example2
def squa(a):
    return a*a
numbers=[2,4,3,5,6,7,66,44,45]
square=list(map(squa,numbers))
print(square)

# output is [4, 16, 9, 25, 36, 49, 4356, 1936, 2025]


# example3
#using lambda function with map function

numbers=[2,4,3,5,6,7,66,44,45]
square=list(map(lambda x: x*x, numbers))
print(square)

#output is- [4, 16, 9, 25, 36, 49, 4356, 1936, 2025]



#example4

def square(a):
    return a*a

def cube(a):
    return a*a*a

func=[square,cube]

for i in range(5):
    val=list(map(lambda x:x(i),func))
    print(val)

#output is
[0, 0]
[1, 1]
[4, 8]
[9, 27]
[16, 64]


#Use of filter function
lis1=[1,2,3,4,5,6,7,8,9]

def is_greater_5(num):
    return num>5

gr_than_5=list(filter(is_greater_5,lis1))

print(gr_than_5)

#output is [6, 7, 8, 9]

"""

#Use of reduce function

from functools import reduce

lis1=[1,2,3,4,5,8,9,10]
num=reduce(lambda x,y:x+y,lis1)

print(num)

#output is 42
