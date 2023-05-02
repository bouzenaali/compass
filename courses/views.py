from django.shortcuts import render
from . serializers import *
from . models import *
from rest_framework import generics
from rest_framework.views import APIView 
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from accounts.models import Teacher
from django.contrib.auth.models import Group, Permission
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required


# Create your views here.

#create course


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
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            description = serializer.validated_data.get('description')
            c_levels_ids = request.data.get('c_levels')
            c_groups_ids = request.data.get('c_groups')
            c_sessions_ids = request.data.get('c_sessions')

            # Check if a course with the same name already exists
            if Course.objects.filter(name=name).exists():
                return Response({'success': False, 'message': 'A course with the same name already exists'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the levels exist
            if not Level.objects.filter(id__in=c_levels_ids).count() == len(c_levels_ids):
                return Response({'success': False, 'message': 'Invalid level IDs'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the groups exist
            if not Group.objects.filter(id__in=c_groups_ids).count() == len(c_groups_ids):
                return Response({'success': False, 'message': 'Invalid group IDs'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the sessions exist
            if c_sessions_ids and not Session.objects.filter(id__in=c_sessions_ids).count() == len(c_sessions_ids):
                return Response({'success': False, 'message': 'Invalid session IDs'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the Course object
            course = serializer.save()

            # Add levels to the course
            for level_id in c_levels_ids:
                course.c_levels.add(Level.objects.get(id=level_id))

            # Add groups to the course
            for group_id in c_groups_ids:
                course.c_groups.add(Group.objects.get(id=group_id))

            # Add sessions to the course
            for session_id in c_sessions_ids:
                course.c_sessions.add(Session.objects.get(id=session_id))

            return Response({'course': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






@method_decorator(permission_required('courses.change_Level'),name='dispatch')
class addLevel(APIView):
    def post(self, request):
        serializer = LevelSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')

            # Check if the level already exists
            if Level.objects.filter(name=name).exists():
                return Response({'success': False, 'message': 'Level already exists'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the Level object
            level = serializer.save()
            return Response({'level': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@method_decorator(permission_required('courses.change_Group'),name='dispatch')       
class addGroup(APIView):
    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            g_level_id = request.data.get('g_level')
            g_teacher_id = request.data.get('g_teacher')

            # Check if the level exists
            if not Level.objects.filter(id=g_level_id).exists():
                return Response({'success': False, 'message': 'Invalid level ID'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the teacher exists
            if not Teacher.objects.filter(id=g_teacher_id).exists():
                return Response({'success': False, 'message': 'Invalid teacher ID'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the group already exists
            if Group.objects.filter(name=name, g_level_id=g_level_id).exists():
                return Response({'success': False, 'message': 'Group already exists'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the Group object
            group = serializer.save()
            return Response({'group': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#create session 
@method_decorator(permission_required('courses.change_Session'),name='dispatch')
class addSession(APIView):
    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            s_group_id = request.data.get('s_group')
            s_teacher_id = request.data.get('s_teacher')
            date = serializer.validated_data.get('date')
            start_at = serializer.validated_data.get('start_at')
            end_at = serializer.validated_data.get('end_at')
            s_description = serializer.validated_data.get('s_description')
            s_courses_ids = request.data.get('s_courses')
            # Check if session with the same name already exists
            if Session.objects.filter(name=name, s_group_id=s_group_id, s_teacher_id=s_teacher_id, date=date, start_at=start_at, end_at=end_at, s_description=s_description).exists():
                return Response({'success': False, 'message': 'Session with the same name already exists'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the group exists
            if not Group.objects.filter(id=s_group_id).exists():
                return Response({'success': False, 'message': 'Invalid group ID'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the teacher exists
            if s_teacher_id and not Teacher.objects.filter(id=s_teacher_id).exists():
                return Response({'success': False, 'message': 'Invalid teacher ID'}, status=status.HTTP_400_BAD_REQUEST)

            # Check if the courses exist
            if s_courses_ids and not Course.objects.filter(id__in=s_courses_ids).count() == len(s_courses_ids):
                return Response({'success': False, 'message': 'Invalid course IDs'}, status=status.HTTP_400_BAD_REQUEST)

            # Create the Session object
            session = serializer.save()

            # Add courses to the session
            for course_id in s_courses_ids:
                session.s_courses.add(Course.objects.get(id=course_id))

            return Response({'session': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

