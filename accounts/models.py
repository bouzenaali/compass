from django.db import models

# Create your models here.

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return self.name + " " + str(self.grade)
    

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return self.name + " " + self.subject
    

class admin():
    def __init__(self, name, age):
        super().__init__(name, age)

    def __str__(self):
        return self.name