class Dog:
    test = 5




    @classmethod
    def retTet(cls):
        return cls.test

    def __init__(self, a):
        self.a = a

    def mytype(self):
        print(self.test)

class Chihuahua(Dog):

    tester = 5

    @property
    def name(self):
        return self.a

    @name.setter
    def name(self, name):
        self.a = name

    @staticmethod
    def retweet():
        print("I am here")

    def bark(self):
        print("Woof")

    def mytype(self):
        super().mytype()
        print("Jesus Christ")