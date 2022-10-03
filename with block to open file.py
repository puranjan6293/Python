#use of with block to open python file

with open("harry.txt") as f:
    a=f.readline()
    print(a)

#we use this function , because now we dont have to close this file. it is autometicly closed after this