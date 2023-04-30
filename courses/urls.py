from django.urls import path
from . views import *

urlpatterns = [
    path("addCourse",addCourse.as_view(),name="addCourse"),
    path("addLevel",addLevel.as_view(),name="addLevel"),
    path("addGroup",addGroup.as_view(),name="addGroup"),
    path("addSession",addSession.as_view(),name="addSession"),
    path("CourseList",CourseList.as_view(), name="CourseList"),
    path("GroupList",GroupList.as_view(), name="GroupList"),
    path("SessionList",SessionList.as_view(), name="SessionList"),
    path("levelList",LevelList.as_view(), name="LevelList"),
    path("levelOp/<int:pk>",LevelRetrieveUpdateDestroyView.as_view(),name="LevelOp"),
    path("CourseOp/<int:pk>",CourseRetrieveUpdateDestroyView.as_view(),name="CourseOp"),
    path("SessionOp/<int:pk>",SessionRetrieveUpdateDestroyView.as_view(),name="SessionOp"),
    path("GroupOp/<int:pk>",GroupRetrieveUpdateDestroyView.as_view(),name="GroupOp")
]