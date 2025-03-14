class Pet:
    _total_pets = 0

    @classmethod
    def total_pets(cls):
        return cls._total_pets

class Cat(Pet):
    def __init__(self, name):
        self.__class__._total_pets += 1
        self._name = name
        print(super().total_pets())

# what does this code output and why        cls         Pet
a_cat = Cat('Cat1')             # 1         # 1         0
b_cat = Cat('Cat2')             # 2         # 1         0
print(Pet.total_pets())         # 1         # 0         0
print(Cat.total_pets())         # 2         # 2         0
print(Pet._total_pets)          # 2         # 0         0
print(Cat._total_pets)          # Error     # 2         2
print(b_cat.total_pets())       # Error     # 2         0
print(b_cat._total_pets)        # 2         # 2         2 



# ============================================

class Pet:
    _total_pets = 0

    @classmethod
    def total_pets(cls):
        return cls._total_pets

class Cat(Pet):
    def __init__(self, name):
        self.__class__._total_pets += 1
        Pet._total_pets += 1
        self._name = name
        print(super().total_pets())

class Dog(Pet):
    def __init__(self, name):
        self.__class__._total_pets += 1
        Pet._total_pets += 1
        self._name = name
        print(super().total_pets())

# what does this code output and why        cls 
a_cat = Cat('Cat1')             # 1         # 
b_cat = Cat('Cat2')             # 2         # 
a_dog = Dog('Dog1')             # 3
b_dog = Dog('Dog2')             # 4
print(Pet.total_pets())         # 4
print(Pet._total_pets)          # 4 
print(a_cat._total_pets)        # 2
print(a_cat.total_pets())       # 2
print(b_cat._total_pets)        # 2
print(b_cat.total_pets())       # 2
print(a_dog._total_pets)        # 4
print(a_dog.total_pets())       # 4