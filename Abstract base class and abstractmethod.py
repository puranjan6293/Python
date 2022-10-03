#Abstarct base class and abstract method


from abc import ABCMeta, abstractmethod #abstractmethod is a decorator

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0


class Rectangle:
    Type="Reactangle"

    sides=4
    def __init__(self):
        self.length=6
        self.breadth=7
    def printarea(self):
        return f"Area is {self.length * self.breadth}"

react1=Rectangle()

print(react1.printarea())
