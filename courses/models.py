from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    c_levels = models.ManyToManyField('Level', related_name='courses')
    c_groups = models.ManyToManyField('Group', related_name='courses')
    c_sessions = models.ManyToManyField('Session', related_name='courses',blank=True)

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Group(models.Model):
    number = models.FloatField(max_length=255)
    g_level = models.ForeignKey(Level, on_delete=models.CASCADE)
    g_teacher = models.ForeignKey('accounts.Teacher',on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Session(models.Model):
    name = models.CharField(max_length=255)
    s_group = models.ForeignKey(Group, on_delete=models.CASCADE)
    s_teacher = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE, default=1 )
    date = models.DateTimeField()
    start_at = models.TimeField()
    end_at = models.TimeField()
    s_description = models.TextField(blank=True, null=True)
    s_courses = models.ManyToManyField('Course', related_name='sessions')

    def __str__(self):
        return self.name + " " + str(self.date)

