from django.db import models

# Create your models here.

class Person():
    name = models.CharField(max_length=255)
    phone = models.FloatField()
    mail = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(Person):
    def __str__(self):
        return self.name
    
class Teacher(Person):
    def __str__(self):
        return self.name
    
class admin():
    def __str__(self):
        return self.name