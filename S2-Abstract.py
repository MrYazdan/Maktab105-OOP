# Abstract class ( Factory Class ):
from abc import ABC, abstractmethod, ABCMeta


class BaseClass(ABC):
    """
    Abstract class
    """
    pass


class Shape(BaseClass):
    """
     Shape class

     methods:
        - draw()

    """
    @abstractmethod
    def draw(self):
        raise NotImplementedError("You must implement draw method")


# shape = Shape()

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")


class Rectangle(Shape):
    pass


circle = Circle()

rectangle = Rectangle()