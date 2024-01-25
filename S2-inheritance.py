# simple inherit

class Parent:
    __attrs = ['name', 'age']
    public_attrs = [...]

    pass


class Child(Parent):

    def __init__(self):
        print(self.public_attrs)


python = Child()


# Composition -> composite:

class Email:
    def __init__(self, email: str, provider: str) -> None:
        self.email = email
        self.provider = provider

    def send_mail(self, message: str) -> None:
        print(f"Sending mail to {self.email} from {self.provider} with message: {message}")


class Phone:
    def __init__(self, country_code: str, phone: str, operator: str) -> None:
        self.country_code = country_code
        self.phone = phone
        self.operator = operator


class User:
    def __init__(self, name: str, password: str, age: int) -> None:
        self.name = name
        self.password = password
        self.age = age


class CompositionProfile:
    def __init__(self, email, provider, country_code, phone, operator, first_name, last_name, age):
        self.email = Email(email, provider)
        self.phone = Phone(country_code, phone, operator)
        self.User = User(first_name, last_name, age)


my_profile = CompositionProfile(email="LkI5H@example.com",
                                provider="gmail",
                                country_code="98",
                                phone="09139999999",
                                operator="MCI",
                                first_name="LkI5H",
                                last_name="LkI5H",
                                age=28)

my_profile.email.send_mail("Hello World!")


# Component
class ComponentProfile:
    def __init__(self, email, phone, user):
        assert isinstance(email, Email), "email must be an instance of Email"
        self.email = email

        assert isinstance(phone, Phone), "phone must be an instance of Phone"
        self.phone = phone

        assert isinstance(user, User), "user must be an instance of User"
        self.user = user


ali = User("ali", "13701370", 28)
ali_mail = Email("ali1370@gmail.com", "gmail")
ali_phone = Phone("98", "09139999999", "MCI")

ali_profile = ComponentProfile(ali_mail, ali_phone, ali)
ali_profile.email.send_mail("Hello World!")


# Mixins:
class Gun:
    pass


class Bag:
    pass


# class SnipeGUN(Gun, ScopeMixin, UpgradableMixin):
#     Bag = Bag()


class X:
    pass


class Y:
    pass


class A(X, Y):
    def salam(self):
        print("Super salam in A")
        return super().salam()


class B(A):
    def salam(self):
        return "Salam in B"


class C:
    def salam(self):
        print("Super salam in C")
        return "Salam in C"


class D(B, C):
    def __init__(self):
        print(super().salam())


d = D()
print(D.__mro__)
