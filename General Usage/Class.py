class Dog:
    test = 5

    def __init__(self, a):
        self.a = a

    def mytype(self):
        print(self.test)

class Chihuahua(Dog):
    def bark(self):
        print("Woof")