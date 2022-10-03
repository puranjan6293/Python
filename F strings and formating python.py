# F Strings
"""
#normal type

me="Harry"
a="this is %s"%me
print(a)

#output-
this is Harry

#Lets use

me="Harry"
a1=3
a="this is %s %s"%(me,a1)
print(a)



# Lets use format

me="Harry"
a1=3
a="this is {} {}"
b=a.format(me,a1)
print(b)

#output is- this is Harry 3



#The aboves are also not good
#So lets use F strings

me="Harry"
a1=3
a=f"this is {me} {a1}"
print(a)

#output is- this is harry 3

"""
#lets go highlevel

me="Harry"
a1=3
a=f"this is {me} {a1} {34*47}" #Easy use
print(a)

#output is- this is harry 3 1598