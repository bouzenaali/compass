from django.contrib import admin
from .models import Student, Teacher, Admin


admin.site.register([Student, Teacher, Admin])

