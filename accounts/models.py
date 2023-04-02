from django.db import models
from courses.models import Course
# Create your models here.

class Person():
    name = models.CharField(max_length=255)
    phone = models.FloatField()
    mail = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(Person):
    courses = models.ManyToManyField(Course, related_name='students')
    def __str__(self):
        return self.name
    
class Teacher(Person):
    courses = models.ManyToManyField(Course, related_name='teachers')
    def __str__(self):
        return self.name
    
class Admin():
    def __str__(self):
        return self.name