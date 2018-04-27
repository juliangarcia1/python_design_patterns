import sys

'''
DP  design pattern
Factory.
Object creation,
DP specialize in objects creation

'''

class Dog:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Woof!"

class Cat:
    def __init__(self, name):
        self._name = name

    def speak(self):
        return "Meow"

def get_pet(pet="dog"):
    pets = dict(dog=Dog("Hope"), cat=Cat("Peace"))
    return pets[pet]

def factory():
    d = get_pet("dog")
    print(d.speak())
    c = get_pet("cat")
    print(c.speak())



if __name__ == '__main__':
    factory()
