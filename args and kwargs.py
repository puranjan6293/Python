"""
#Use of args

def useof (*args):
    print(args[3])
har=["harry","rama","sita","priti","jyoti","damayanti"]
useof(*har)

# output is priti


#use of forloop under args

def useof (*args):
    for item in args:
        print(item)

har=["harry","rama","sita","priti","jyoti","damayanti"]
useof(*har)

# output is-
# harry
# rama
# sita
# priti
# jyoti
# damayanti

"""

#Use of kwargs

# def function_name_print(a, b, c, d, e):
#     print(a, b, c, d, e)

def funargs(normal, *argsrohan, **kwargsbala):
    print(normal)
    for item in argsrohan:
        print(item)
    print("\nNow I would Like to introduce some of our heroes")
    for key, value in kwargsbala.items():
        print(f"{key} is a {value}")


# function_name_print("Harry", "Rohan", "Skillf", "Hammad", "Shivam")

har = ["Harry", "Rohan", "Skillf", "Hammad",
       "Shivam", "The programmer"]
normal = "I am a normal Argument and the students are:"
kw = {"Rohan":"Monitor", "Harry":"Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam":"Cook"}
funargs(normal, *har, **kw)