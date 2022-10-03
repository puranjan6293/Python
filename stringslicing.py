
"""
#string
mystr="Harry is a good boy"
print(mystr)

#String slicing
mystr="Harry is agood boy"
print(mystr[0])


#String slicing for multilpe words

mystr="Harry is a good boy"
print(mystr[0:5])

#Note 0 is including but 5 is excluding so here output is 'Harry'

#Advance string slicing

mystr="Harry is a good boy"
print(mystr[0:5:2])
#output is Hry
#because it skip one characters

mystr="Harry is a good boy"
print(mystr[::])

#outputis Harry is a good boy

#because it autometically fill the blanks
#that is [0:length of the string:1]


mystr="Harry is a good boy"
print(mystr[0:8:3])

#output is Hri

#first it print [0:8] , that is   Harry is
#then it skip 2 characters in between  Harry is ,
#so the output is Hri


#Negative string slicing

mystr="Harry is good boy"
print(mystr[0:-5])

#output is Harry is goo

mystr="Harry is a good boy"
print(mystr[::-1])
#Simply it will inverse the output
#Output is yob doohg a si yrraH


mystr="Harry is a good boy"
print(mystr[::-2])

#First it will inverse the output of [:]
#Then it skip one one characters
#the output is ybdo iyrH



#Some importnat functions

mystr="harry is a good boy"
print(mystr.capitalize())

#output is Harry is a good boy


mystr="Harry is a good boy"
print(mystr.replace("is","are"))

#output is Harry are a good boy


mystr="harry is a good boy"
print(mystr.upper())

#output is HARRY IS A GOOD BOY


mystr="Harry is a good boy"
print(mystr.find("is"))

#output is 6


mystr="Harry Is A Good Boy"
print(mystr.lower())

#Output is harry is a good boy

mystr="Harry is a good boy"
print(mystr.endswith("boy"))

#Output is true

"""
