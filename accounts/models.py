from django.db import models
from django.contrib.auth.models import Group

class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.FloatField()
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default='password')

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
    
class SuperUser(Admin):
    
        def __str__(self):
            return self.name

# Create teacher group
teachers_g = Group.objects.create(name='teachers_g')

# Create admin group
admins_g = Group.objects.create(name='admins_g')

# Create superuser group
superusers_g = Group.objects.create(name='superusers_g')