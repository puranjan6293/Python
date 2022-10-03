# File IO basics

"""
"r" - open file for reading (defult mode)
"w" - open file for write
"x" - creates file if not exist
"a" - add more content to the file
"t" - text mode (defult mode)
"b" - binary mode
"+"- read and write both


"""

#question of the day
#How to print docstring

#Ans
def function1(a,b):
    """Point to remember"""
    addition=a+b
    return addition

print(function1.__doc__)
