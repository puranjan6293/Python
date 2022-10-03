#if else & elif functions
var1=5
var2=10

var3=int(input())
if var3>var1:
    print("Greater")
#we can use multiple if function like-
if var3==var1:
    #for checking equality we have to use the equality symble twice . that is ==
    print("equal")
    #if multiple if else function are used in a function that time we use elif function
    #it stop rendering when it found the answer
elif var3>var2:
    print("mostgreater")
    
else: print("lesser")