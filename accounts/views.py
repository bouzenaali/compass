from django.shortcuts import render
from rest_framework import generics
from .models import Student, Teacher,Admin
from courses.models import Course
from .serializers import *
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required


# Create your views here.

#view that lists all students

class StudentList(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# view that retrieves/updates/destroys a student
class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#view that lists all teachers

class TeacherList(generics.ListAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

# view that retrieves/updates/destroys a teacher
class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

#view that lists all Admins

class AdminList(generics.ListAPIView):
    queryset=Admin.objects.all()
    serializer_class=AdminSerializer

# view that retrieves/updates/destroys an Admin
class AdminRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer