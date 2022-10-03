"""
#set

s=set()
print(type(s))

#output is <class 'set'>
#

s_from_list=set([1,2,3,4,5])
print(s_from_list)
#output is {1, 2, 3, 4, 5}


L=[1,2,3,4,5]
s_from_list=set(L)
print(s_from_list)
#output is {1, 2, 3, 4, 5}
#Because we stored in l


#how to add things in set?

s=set()
s.add(1)
s.add(1)
s.add(3)
s.add(5)
s.add(9)
print(s)

#here output is {1, 3, 5, 9}
#Here 1 is printed once because set contain unique values


#Union and intersection
s=set()
s.add(1)
s.add(1)
s.add(3)
s.add(5)
s.add(9)

s.union({1,2,3})
print(s)

#output is {1, 3, 5, 9}
#Here this is printed once because set contain unique values

"""
s=set()
s.add(1)
s.add(1)
s.add(3)
s.add(5)
s.add(9)

s.intersection({1,2,3})
print(s)

#output is {1, 3, 5, 9}

#This is like real intersection