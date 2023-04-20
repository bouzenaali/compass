from django.db import models






class Person(models.Model):
    name = models.CharField(max_length=255)
    phone = models.FloatField()
    mail = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Student(Person):
    courses = models.ManyToManyField('courses.Course', related_name='students',blank=True, null=True)
    is_present = models.BooleanField(default=False) # this field will be changed
    # sessions_attended = models.ManyToManyField('courses.Session', related_name='students',blank=True, null=True)
    def __str__(self):
        return self.name
    
class Teacher(Person):
    courses = models.ManyToManyField('courses.Course', related_name='teachers',blank=True, null=True)
    password = models.CharField(max_length=255, default='password')
    def __str__(self):
        return self.name
    
class Admin(Person):
    password = models.CharField(max_length=255, default='password')
    def __str__(self):
        return self.name


# # this table will track the attendance of students in a session
# class Attendance(models.Model):
#     session = models.ForeignKey('courses.Session', on_delete=models.CASCADE, related_name='attendances')
#     student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='attendances')
#     is_present = models.BooleanField(default=False)
