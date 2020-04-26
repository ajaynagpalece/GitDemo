class Calculator:
    num = 100

    def getData(self):
        print("Method executed in class")


obj = Calculator()              # Syntax to create object in python.
obj.getData()
print(obj.num)

print("----------------------------Constructor----------------------------------")
print("---------------------Added a New line for testing----------------------------")


class Calculator:
    num = 100

    def __init__(self):
        print("Constructor called automatically when object is created")

    def getData(self):
        print("Method executed in class")


obj = Calculator()              # Syntax to create object in python.
obj.getData()
print(obj.num)