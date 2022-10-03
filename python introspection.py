
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithharry.com"

    def explain(self):
        return f"This employee is {self.fname} {self.lname}"

    @property
    def email(self):
        if self.fname==None or self.lname == None:
            return "Email is not set. Please set it using setter"
        return f"{self.fname}.{self.lname}@codewithharry.com"

    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

skillf=Employee("Skill","f")
"""
print(skillf.email)
print(type(skillf))
print(type("This is a string"))
print(id(skillf))
print(id("This is a string"))
O="This is a string"
print(dir("O"))

"""

#LETS IMPORT AN INSPECT MODULES

import inspect
print(inspect.getmembers(skillf))

"""
# TASK
def Inspect_somethingect(something, ch):
    import inspect
    if (ch==1):
        # check whether the arguement is a class or not
        if (inspect.isclass(something)):
            return f"'{something}' is a class."
        
        # check whether the arguement is a module or not
        elif (inspect.ismodule(something)):
            return f"'{something}' is a module."

        # check whether the arguement is a function or not
        elif (inspect.isfunction(something)):
            return f"'{something} is a function."
            
        # check whether the arguement is a method of a class or not
        elif (inspect.ismethod(something)):
            return f"'{something}' is a method."
    
    if (ch==2):
        # returns the class hierarchy
        return f"Hierarchy of {something} object is \n{inspect.getmro(something)}"
    
    if (ch==3):
        # returns all the methods, attributes with values of the class.
        return inspect.getmembers(something)
    
    if (ch==4):
        # returns all the parameters passed to a given function
        return inspect.signature(something)
    
    if (ch==5):
        # returns the source code of given class, module, method, function
        return inspect.getsource(something)
    
    if (ch==6):
        # returns the module name of the method or function passed in it.
        return inspect.getmodule(something)
    
    if (ch==7):
        # returns the docstring of the method.
        return inspect.getdoc(something)

"""