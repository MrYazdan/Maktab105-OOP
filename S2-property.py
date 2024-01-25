# class BankAccount:
#     # Encapsulation:
#     # -> Public
#     # -> Protect ( _ )
#     # -> Private ( __ )
#
#     def __init__(self, name):
#         self.__balance = 0
#         self.name = name
#
#         self.__number_ = 10
#
#     def _get_balance(self):
#         return self.__balance
#
#
# my_account = BankAccount("Reza Yazdani")
# my_account.__balance = 123
#
# print(my_account._get_balance())

from time import sleep


import uuid

class User:
    @staticmethod
    def _username_validator(username: str) -> bool:
        return isinstance(username, str) and len(username) >= 8 and username.isidentifier()

    @staticmethod
    def _password_validator(password: str) -> bool:
        return isinstance(password, str) and 4 <= len(password) <= 8

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

        self.__id = uuid.uuid4().hex

    @property
    def id(self):
        return self.__id

    @property
    def username(self) -> str:
        return f"({self.__username}#)"

    @username.setter
    def username(self, new_username: str) -> None:
        assert self._username_validator(new_username), "Username not valid !"
        self.__username = new_username

    @property
    def password(self):
        return hash(self.__password)

    @password.setter
    def password(self, new_password):
        assert self._password_validator(new_password), "Password not valid !"
        self.__password = new_password

    # password = property(password, set_password)


# def change_password(self, old_password: str, new_password: str) -> None:
#     assert self.password == hash(old_password), "Passwords not matched !"
#     assert self._password_validator(new_password), "Password not valid !"
#     self.__password = new_password


fardin = User("fardin_zand", "122456")
fardin.username = "falconer"

print(fardin.username)
print(fardin.password)

fardin.password = "1231312"
print(fardin.password)

print(fardin.id)

zahra = User("zahra__uuid", password="123dsfs")
print(zahra.id)

zahra.username = "zahra_tehrani"