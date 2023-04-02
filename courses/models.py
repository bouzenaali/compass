from django.db import models
from accounts.models import Teacher
# Create your models here.

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    levels = models.ManyToManyField('Level', related_name='courses')
    groups = models.ManyToManyField('Group', related_name='courses')
    sessions = models.ManyToManyField('Session', related_name='courses')

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField()
    start_at = models.TimeField()
    end_at = models.TimeField()
    description = models.TextField(blank=True, null=True)
    courses = models.ManyToManyField('Course', related_name='sessions')

    def __str__(self):
        return self.name + " " + str(self.date)
