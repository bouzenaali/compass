from django.urls import path, include
from . views import *

urlpatterns = [
    path('/add/student',create_student, name='student'),
    path('/add/teacher',create_teacher, name='teacher'),
    path('/add/admin',create_admin, name='admin'),
]
