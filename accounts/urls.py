from .views import *
from django.urls import path

urlpatterns = [
    path('StudentList',StudentList.as_view(),name='StudentList'),
    path('TeacherList',TeacherList.as_view(),name='TeacherList'),
    path('AdminList',AdminList.as_view(),name='AdminList'),
    path('StudentOp/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='StudentOp'),
    path('TeacherOp/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='TeacherOp'),
    path('AdminOp/<int:pk>/', StudentRetrieveUpdateDestroyView.as_view(), name='AdminOp'),
]