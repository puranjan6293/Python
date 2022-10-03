"""

list1=["Harry",15,"dog",25,50,"marry",3,5]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)

#or we can write

list1=["Harry",15,"dog",25,50,"marry",3,5]
for item in list1:
    if type(item) == int and item > 6:
        print(item)

#made by me
list1=["harry","marry","sarry","besty",10,23,43,56,6,3,4,5,6,7,8,"doggy",5,4,3,3,2]
for item in list1:
    if type(item)==int and item>6:
        print(item)

#output is
23
43
56
7
8

"""

