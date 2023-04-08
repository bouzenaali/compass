from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission





class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.FloatField()
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255, default='password')

    def __str__(self):
        return self.name
    
class Student(Person):
    courses = models.ManyToManyField('courses.Course', related_name='students',blank=True, null=True)
    is_present = models.BooleanField(default=False)
    def __str__(self):
        return self.name
    
class Teacher(Person):
    courses = models.ManyToManyField('courses.Course', related_name='teachers',blank=True, null=True)

    def __str__(self):
        return self.name
    
class Admin(Person):

    def __str__(self):
        return self.name
    
class SuperUser(Admin):
    
        def __str__(self):
            return self.name

# roles
class User(AbstractUser):
    STUDENT = 1
    TEACHER = 2
    ADMIN = 3
    SUPERUSER = 4

    ROLE_CHOICES = (
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'),
        (SUPERUSER, 'superuser')
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=STUDENT)

    # add related_name to avoid clashes with auth.User
    groups = models.ManyToManyField(
        Group,
        related_name='accounts_users_groups',
        blank=True,
        verbose_name=('groups'),
        help_text=(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
    ),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='accounts_users_permissions',
        blank=True,
        verbose_name=('user permissions'),
        help_text=('Specific permissions for this user.'),
    )