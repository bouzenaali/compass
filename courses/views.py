from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework import generics
from rest_framework.views import APIView 
from django.http.response import JsonResponse

# Create your views here.

#create course
class addCourse(APIView):
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        c_levels = request.data.get('level')
        c_groups = request.data.get('group')
        c_sessions = request.data.get('sessions')

        # Vérifie si l'objet existe déjà
        if Course.objects.filter(name=name).exists():
            return JsonResponse({'success': False, 'message': 'Course already exists'})

        # Créer un nouvel objet "Course"
        course = Course.objects.create(
            name=name,
            description=description,
        )

        # Ajouter les relations ManyToMany s'il y en a
        if c_levels:
            for level in c_levels.split(','):
                course.c_levels.add(int(level))
        if c_groups:
            for group in c_groups.split(','):
                course.c_groups.add(int(group))
        if c_sessions:
            for session in c_sessions.split(','):
                course.c_sessions.add(int(session))

        return JsonResponse({'success': True, 'message': 'Course created successfully'})


# views that lists existing courses/levels/groups/sessions

class CourseList (generics.ListAPIView):
     queryset=Course.objects.all()
     serializer_class=CourseSerializer

class LevelList (generics.ListAPIView):
     queryset=Level.objects.all()
     serializer_class=LevelSerializer
     

class GroupList (generics.ListAPIView):
     queryset=Group.objects.all()
     serializer_class=GroupSerializer
     

class SessionList (generics.ListAPIView):
     queryset=Session.objects.all()
     serializer_class=SessionSerializer
      
#views that retrieve/update/destroy a course/level/session/group

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Course.objects.all()
    serializer_class = CourseSerializer

class LevelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class SessionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

class GroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

