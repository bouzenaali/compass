from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.FloatField()
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(Person):
    courses = models.ManyToManyField('courses.Course', related_name='students')
    is_present = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Teacher(Person):
    courses = models.ManyToManyField('courses.Course', related_name='teachers')

    def __str__(self):
        return self.name
    
class Admin(Person):

    def __str__(self):
        return self.name