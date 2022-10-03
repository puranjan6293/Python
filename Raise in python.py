#RAISE IN PYTHON
"""
a = input("What is your name\n")
if a.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"Hello {a}")

#output is-
# What is your name
# Puranjan
# Hello Puranjan
#if number input than output is
#   raise Exception("Numbers are not allowed")
# Exception: Numbers are not allowed

"""
# Task - Write about 2 built in exception

c = input("Enter your name")
try:
    print(a)

except Exception as e:

    if c =="harry":
        raise ValueError("Harry is blocked he is not allowed")

    print("Exception handled")