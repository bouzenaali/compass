from django.contrib import admin
from .models import Course, Level, Group, Session

admin.site.register(Course)
admin.site.register(Level)
admin.site.register(Group)
admin.site.register(Session)