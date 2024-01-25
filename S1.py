"""
user : name, password, age, phone
"""
from typing import Callable


# ali = ("ali", '13701370', 28, '09139999999')

# user += is_active : bool

# ali = ("ali", '13701370', 28, '09139999999', True)
#
# ali[-2]

# def profile(user: dict):
#     return f"{user['name']}, Age: {user['age']}"

# ali = {
#     "name": "ali",
#     "password": '13701370',
#     "age": 28,
#     "phone": '09139999999',
#     "is_active": True,
#     "profile": lambda user: f"{user['name']}, Age: {user['age']}"
# }

# ali['is_active'] = False
# # ali["profile"] = profile
# print(ali["profile"](ali))

class User:
    def __init__(self, name, password, age, phone, is_active):
        self.name = name
        self.password = password
        self.age = age
        self.phone = phone
        self.is_active = is_active

    def profile(self):
        return f"{self.name}, Age: {self.age}"


ali = User(
    name="ali",
    password='13701370',
    age=28,
    phone='09139999999',
    is_active=True
)

# print(ali.name)
ali.email = "ali@email.dev"


# def say_hello(user: User):
#     print(f"Hi {user.name} :)")


# ali.say_hello = say_hello
# print(ali.email)
# ali.say_hello(ali)

class Student:
    # class attrs
    students = []

    # def get_student(self):
    #     print("in instance method")
    #     return self.students

    @classmethod
    def get_student(cls):
        print(cls)

        print("in class method")
        return cls.students

    def __repr__(self):
        return f"<{self.__class__.__name__}: {self.name}>"

    def __init__(self, name, age):
        # instance attrs
        self.name = name
        self.age = age
        # self.students = []

        # add to
        # print(Student == self.__class__)

        self.__class__.students.append(self)
        # self.students.append(self)

    def profile(self):
        return f"{self.name}, Age: {self.age}"


ali = Student("ali javaii", 35)
reza = Student("Reza junior", 21)
fatemeh = Student("Fati php", age=30)

# Student.students = [ali, reza, fatemeh]

# print(Student.students)

numbers = [1, 7, 9, 3, 5, -9, 23]


# in-place method
# numbers.sort()  # 1. -> None | 2. self persist

# new_numbers = numbers.sort()
# print(numbers)

# out-place method
# numbers = sorted(numbers)  # 1. -> sorted data | 2. global access
# print(numbers)
#
# string = "alpha"
#
# numbers_two = (1, 2, 4, 76, -4)
#
#
# print(type(sorted(numbers_two)))

# print(Student.get_student())
# print(ali.get_student())

def printer(shape):
    print(f"<{shape.name}>")


class Shape:
    shapes = []

    # printer = printer

    @staticmethod
    def printer(obj):
        return f"<{obj.name}>" if obj else "Name is empty !"

    # def printer(self=None):
    #     return f"<{self.name}>" if self else "Name is empty !"

    def __init__(self, name):
        self.name = name

        self.shapes.append(self)


# print(Student.students[1].profile())
# print(Student.profile())

rectangle = Shape("Rectangle")


# rectangle.printer()

# print(rectangle.printer(rectangle))
# print(Shape.printer() is rectangle.printer())

class Singleton:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    # def __init__(self, *args, **kwargs):
    #     if not self.__class__.__instance:
    #         self.__class__.__instance = self
    #
    #     instance = self.__class__.__instance
    #     self = instance


class Logger(Singleton):
    pass


root_logger = Logger()
my_logger = Logger()
your_logger = Logger()


# print(id(root_logger), id(my_logger), id(your_logger), sep="\n")

class Application:
    hooks = {
        'start': [],
        'finish': []
    }

    def __init__(self, _callable: Callable):
        self.callable = _callable

    def __call__(self, *args, **kwargs):
        for _callable in self.__class__.hooks['start']:
            _callable()

        self.callable(*args, **kwargs)

        for _callable in self.__class__.hooks['finish']:
            _callable()


Application.hooks['start'].append(lambda: print("Before start application\n"))
Application.hooks['finish'].append(lambda: print("\nFinished application"))


def main():
    print("Welcome to my calculator\n- Enter your sequence\n")
    print(eval(input("> ")))


app = Application(main)


# app()


class A:
    def __call__(self):
        print("A seda zade shod !")


a = A()
# a()

# print(callable(a))

from os import system as terminal


class Console:
    def __call__(self, commands):
        if 'rm' in commands:
            raise Exception("Dont use rm command !")
        return terminal(" ".join(commands))


safe_console = Console()
safe_console(['cat', '/etc/lsb-release'])
# safe_console(['rm', '/'])
safe_console(['echo', 'Ajab !'])
