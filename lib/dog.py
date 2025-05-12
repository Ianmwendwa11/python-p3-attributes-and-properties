#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", age=0, breed="Pug"): 
        self.name = name
        self.age = age
        self.breed = breed

    # name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = None

    name = property(get_name, set_name)

    # age property
    def get_age(self):
        return self._age

    def set_age(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 120:
            self._age = value
        else:
            print("Age must be a number between 0 and 120.")
            self._age = None

    age = property(get_age, set_age)

    # breed property
    def get_breed(self):
        return self._breed

    def set_breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = None

    breed = property(get_breed, set_breed)
