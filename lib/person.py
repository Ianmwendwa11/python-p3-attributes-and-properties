#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Unknown", age=0, job=None):
        self.name = name
        self.age = age
        self.job = job

    # name property
    def get_name(self):
        return self._name

    def set_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    # age property
    def get_age(self):
        return self._age

    def set_age(self, value):
        if isinstance(value, (int, float)) and 0 <= value <= 120:
            self._age = value
        else:
            print("Age must be a number between 0 and 120.")

    age = property(get_age, set_age)

    # job property
    def get_job(self):
        return self._job

    def set_job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")

    job = property(get_job, set_job)
