from django.db import models

# Create your models here.

class course():
    def __init__(self, name, code, description, teacher, students):
        self.name = name
        self.code = code
        self.description = description
        self.teacher = teacher
        self.students = students

    def __str__(self):
        return self.name + " " + self.code + " " + self.description + " " + self.teacher + " " + self.students