
"""
i=0
while (i<45):
    print(i, end=(" "))
    i=i+1

#output is
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44


#Lets use while function
i=0
while (True): #while(True) functin are the function jo hamesa chalta rehta hai
    print(i, end=(" "))
    if i==45:
        break #stop the loop
    i=i+1

#output is
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45


#Lets use continue function
i=0
while(True):
    if i+1<5:
        i=i+1
        continue
    print(i+1, end=(" "))
    if i==44:
        i=i+1
        break
    i=i+1

#output is
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45

"""
