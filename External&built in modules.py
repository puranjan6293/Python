#Using external and builtin modules
"""
#Random number generator
#case1
import random

random_number=random.randint(0,5)
print(random_number)


#case2
import random

random_number=random.randint(0,1)
rand=random.random()
#If we want to generate random no from 0 to 100 than we just do it like
#rand=random.random()*100
print(rand)



#Use of random.choice
import random

l=["Youtube","Faceboom","Instagram","Twiter","Study"]

p=random.choice(l)
print(p)



#Tsak

#Using emoji module

from emoji import emojize
print(emojize(":thumbs_up:"))

print("achha laga naa?")

#output
# 👍
# achha laga naa?



# Statistics module with its two functions
import statistics
# first function
data=[10, 15, 25, 25, 275, 325, 475]
stat=statistics.pstdev(data)        # The pstdev returns the population standard deviation in short the sqare root of the population varience
print(stat)                         # if we need to retrive the avarage growth of population in some areas than this fuction can be very useful.

# Second function
geomet=statistics.geometric_mean(data)
print(geomet)                       # It basically finds the avarage of the given data unlike arithemetic mean it also
                                    # finds the acurate avarage while in percentage. It is generally used to determine
                                    # the performance result of and investment of portfolio.



# platform module and its functions
import platform
print("processor is :", platform.processor())
print("architecture  is :", platform.architecture())
print("system is :", platform.system())
print("compiler is :", platform.python_compiler())


#Using turtle function
import turtle

abhi = turtle.Turtle()
abhi.speed(0)
abhi.color("purple", "blue")  # this is for colour
abhi.begin_fill()

for i in range(100):
    abhi.forward(200)
    abhi.left(168.5)
    abhi.forward(200)
    abhi.left(175)

abhi.penup()
abhi.forward(200)
abhi.pendown()
for i in range(100):
    abhi.forward(200)
    abhi.left(168.5)
    abhi.forward(200)
    abhi.left(175)

abhi.end_fill()

abhi = turtle.Turtle()
abhi.color("cyan", "green")
abhi.begin_fill()
abhi.forward(100)
abhi.left(90)
abhi.forward(100)
abhi.left(90)
abhi.forward(100)
abhi.left(90)
abhi.forward(100)

abhi.penup()
abhi.forward(100)
abhi.pendown()

abhi.forward(100)
abhi.setheading(90)
abhi.forward(100)
abhi.left(90)
abhi.forward(100)
abhi.left(90)
abhi.forward(100)
abhi.left(90)
abhi.forward(100)
abhi.end_fill()

turtle.done()



#Using calender module
import calendar
print("which year calender you need")
year = int(input("enter year \n"))
cldr = calendar.calendar(year)
print(cldr)



#Using math modules
import math
a=int(input("Factorial off\n"))
sol = math.factorial(a)
print("Factorial: ", sol)

import time

print("This is printed immediately.")
time.sleep(2.4)
print("This is printed after 2.4 seconds.")

"""

# Python Text to Speech

import pyttsx3
while True:
    text = input("Enter Line = ")
    friend = pyttsx3.init()
    friend.say(text)
    friend.runAndWait()
    friend.stop()