#DIAMOND SHAPE PROBLEM IN PYTHON

class A:
    def meth(self):
        print('This is the method from class A')

class B(A):
    def meth(self):
        print('This is the method from class B')

class C(A):
    def meth(self):
        print('This is the method from class C')

class D(B,C):
    def meth(self):
        print('This is the method from class D')


a=A()
b=B()
c=C()
d=D()

d.meth()
