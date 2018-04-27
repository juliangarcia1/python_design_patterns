'''
Abstract factory
When  a client expects to received a family of related objects
but dont have to know until runtime
'''

class Dog:

    def speak(self):
        return 'Woof!'

    def __str__(self):
        return "Dog"
class Cat:

    def speak(self):
        return 'Meow!'

    def __str__(self):
        return "Cat"

class DogFactory:

    def get_pet(self):
        return Dog()

    def get_food(self):
        return "Dog Food"

class CatFactory:

    def get_pet(self):
        return Cat()

    def get_food(self):
        return "Cat Food"

class PetStore:

    def __init__(self, pet_factory = None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print('Our pet is {}'.format(pet))
        print('Our pet say hello by {}'.format(pet.speak()))
        print('Its food is {}'.format(pet_food))


def abstract_factory():
    #Get concrete factory instance
    factory = CatFactory()

    # create petstore to pass the factory
    pet_store = PetStore(factory)

    pet_store.show_pet()

if __name__ == '__main__':
    abstract_factory()


