"""
f=open("harry.txt")
content=f.read()
print(content)

f.close()

#Advanced

f = open("harry.txt", "rt")
print(f.readlines())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# content = f.read()
#
# for line in f:
#     print(line, end="")
# print(content)
# content = f.read(34455)
# print("1", content)
#
# content = f.read(34455)
# print("2", content)
f.close()


#lets practice

f=open("harry.txt","rt")
content=f.read()
print(content)


# for line by line print

f=open("harry.txt","rt")
for line in f:
    print(line,end="")

"""
#read line function
f=open("harry.txt","rt")
print(f.readline())
print(f.readline())


f.close()