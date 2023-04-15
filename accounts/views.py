from django.contrib.auth.models import User,Permission
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Student, Teacher, Admin
from django.contrib.auth.models import Group



# Create the groups
teachers_group, created = Group.objects.get_or_create(name='teachers')
admins_group, created = Group.objects.get_or_create(name='admins')
        
@api_view(['POST'])
@permission_required('accounts.add_Person')
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        
        # Check if the user already exists
        try:
            student = Student.objects.get(name=name)
            return Response({'success':False, 'message': 'Student already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Student.DoesNotExist:
            pass

        # Create the Student object
        student = serializer.save()
        return Response({'student': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_required('accounts.add_Person')
def create_teacher(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        password = serializer.validated_data.get('password')
        
        # Check if the user already exists
        try:
            teacher = User.objects.get(username=name)
            return Response({'success':False, 'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        # Create the Teacher object
        teacher = serializer.save()

        # Create the associated User object with the teacher group
        user = User.objects.create_user(username=name, password=password)
        user.groups.add(teachers_group)

        # Associate the user with the created teacher object
        teacher = serializer.save(user=user)

        return Response({'teacher': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
@permission_required('accounts.add_Person')
def create_admin(request):
    serializer = AdminSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data.get('name')
        password = serializer.validated_data.get('password')
        
        # Check if the user already exists
        try:
            admin = User.objects.get(username=name)
            return Response({'success':False, 'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        # Create the Teacher object
        admin = serializer.save()

        # Create the associated User object with the teacher group
        user = User.objects.create_user(username=name, password=password)
        user.groups.add(admins_group)

        # Associate the user with the created teacher object
        teacher = serializer.save(user=user)

        return Response({'admin': serializer.data}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_required('accounts.change_Student')
def edit_student_attendance(request, student_id):
    # modifier l'absence et la presence des etudiants
    # il faut voir qvel es que l'etudiant ni n le group ines negh khati
    #...
    return JsonResponse({'success': True})