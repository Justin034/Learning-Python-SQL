# Testing locality in terms of the effects of self.x vs just x

class Robot:
    def __init__(self, name):
        self.name = name  # Binds 'name' to the specific instance


    def rename(self, name):
        self.name = name
        print(f"Name is changed to {name}")

    def introduce(self):
        # Accesses the instance variable using self
        print(f"Hello, my name is {self.name}.")


# Creating two distinct objects
robot1 = Robot("Alpha")
robot2 = Robot("Beta")

robot1.introduce()  # Outputs: Hello, my name is Alpha.
robot2.introduce()  # Outputs: Hello, my name is Beta.

robot1.rename("Jonny")

robot1.introduce()