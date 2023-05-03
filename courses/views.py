from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework import generics
from rest_framework.views import APIView 
from django.http.response import JsonResponse
from django.contrib.auth.models import Group, Permission
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required



# Create the groups
teachers_group, created = Group.objects.get_or_create(name='teachers')
admins_group, created = Group.objects.get_or_create(name='admins')

# Add the permissions to the groups
admins_group.permissions.set(Permission.objects.filter(codename__in=['change_Course', 'change_Level', 'change_Group', 'change_Session','add_Course', 'add_Level', 'add_Group', 'add_Session','delete_Course', 'delete_Level', 'delete_Group', 'delete_Session','view_Course', 'view_Level', 'view_Group', 'view_Session']))
teachers_group.permissions.set(Permission.objects.filter(codename__in=['view_Course', 'view_Level', 'view_Group', 'view_Session']))


#create course
@method_decorator(permission_required('courses.change_Course'),name='dispatch')
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
@method_decorator(permission_required('courses.view_Course'),name='dispatch')
class CourseList (generics.ListAPIView):
     queryset=Course.objects.all()
     serializer_class=CourseSerializer

@method_decorator(permission_required('courses.view_Level'),name='dispatch')
class LevelList (generics.ListAPIView):
     queryset=Level.objects.all()
     serializer_class=LevelSerializer
     
@method_decorator(permission_required('courses.view_Group'),name='dispatch')
class GroupList (generics.ListAPIView):
     queryset=Group.objects.all()
     serializer_class=GroupSerializer
     
@method_decorator(permission_required('courses.view_Session'),name='dispatch')
class SessionList (generics.ListAPIView):
     queryset=Session.objects.all()
     serializer_class=SessionSerializer
      
#views that retrieve/update/destroy a course/level/session/group
@method_decorator(permission_required('courses.change_Course'),name='dispatch')
@method_decorator(permission_required('courses.delete_Course'),name='dispatch')
@method_decorator(permission_required('courses.view_Course'),name='dispatch')
class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset =Course.objects.all()
    serializer_class = CourseSerializer

@method_decorator(permission_required('courses.change_Level'),name='dispatch')
@method_decorator(permission_required('courses.delete_Level'),name='dispatch')
@method_decorator(permission_required('courses.view_Level'),name='dispatch')
class LevelRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

@method_decorator(permission_required('courses.change_Session'),name='dispatch')
@method_decorator(permission_required('courses.delete_Session'),name='dispatch')
@method_decorator(permission_required('courses.view_Session'),name='dispatch')
class SessionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

@method_decorator(permission_required('courses.change_Group'),name='dispatch')
@method_decorator(permission_required('courses.delete_Group'),name='dispatch')
@method_decorator(permission_required('courses.view_Group'),name='dispatch')
class GroupRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

