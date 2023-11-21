"""
Dylan Franz
CS 100 2023F Section H09
HW 11, November 22, 2023
"""


# Problem 1

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

sugar = Dog('Sugar', 'border collie')
print(sugar.name)
print(sugar.breed)


# Problem 2

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []

sugar = Dog('Sugar', 'border collie')
print(sugar.tricks)


# Problem 3

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
    def teach(self, trick):
        self.tricks.append(trick)
        print("{} knows {}".format(self.name, trick))

sugar = Dog('Sugar', 'border collie')
sugar.teach('frisbee')
print(sugar.tricks)


# Problem 4

import string
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
    def teach(self, trick):
        self.tricks.append(trick.lower())
        print("{} knows {}".format(self.name, trick))
    def knows(self, trick):
        if trick.lower().strip().strip(string.punctuation) in self.tricks:
            print("Yes, {} knows {}".format(self.name, trick))
            return True
        else:
            print("No, {} doesn't know {}".format(self.name, trick))
            return False

sugar = Dog('Sugar', 'border collie')
sugar.teach('Jump')
print(sugar.tricks)
print(sugar.knows('jump!'))
print(sugar.knows('arithmatic'))


# Problem 5

class Dog:
    species = 'Canis familiaris'
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.tricks = []
    def teach(self, trick):
        self.tricks.append(trick.lower())
        print("{} knows {}".format(self.name, trick))
    def knows(self, trick):
        if trick.lower().strip().strip(string.punctuation) in self.tricks:
            print("Yes, {} knows {}".format(self.name, trick))
            return True
        else:
            print("No, {} doesn't know {}".format(self.name, trick))
            return False

sugar = Dog('Sugar', 'border collie')
print(Dog.species)
print(sugar.species)