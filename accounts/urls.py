from django.urls import path, include
from . views import *

urlpatterns = [
    path('add/student',create_student, name='student'),
    path('add/teacher',create_teacher, name='teacher'),
    path('add/admin',create_admin, name='admin'),
    ##
    path('StudentList',StudentList.as_view(),name='StudentList'),
    path('TeacherList',TeacherList.as_view(),name='TeacherList'),
    path('AdminList',AdminList.as_view(),name='AdminList'),
    path('StudentOp/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='StudentOp'),
    path('TeacherOp/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='TeacherOp'),
    path('AdminOp/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='AdminOp'),
]
