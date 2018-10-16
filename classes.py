# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor - self pertains to class instance
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
    # Method
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1

# Init user object
mohs = User('Mohs Akhtar', 'mohs.akhtar@gmail.com', 27)
janet = User('Janet Jackson', 'jj@gmail.com', 26)

# Edit property
mohs.age = 28

# Call method
print(mohs.greeting)

janet.has_birthday()        # 27


# Customer class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

# Init customer
john = Customer('John Doe', 'j@email.com', 40)

john.set_balance(500)