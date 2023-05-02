from django.contrib.auth.models import User,Permission
from django.http import JsonResponse
from django.contrib.auth.decorators import permission_required
from . serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import Student, Teacher, Admin
from django.contrib.auth.models import Group
from rest_framework import generics
from courses.models import Course
from django.utils.decorators import method_decorator


# Create your views here.

# Create the groups
teachers_group, created = Group.objects.get_or_create(name='teachers')
admins_group, created = Group.objects.get_or_create(name='admins')

# Add the permissions to the groups
teachers_group.permissions.set(Permission.objects.filter(codename__in=['change_student', 'view_student']))
admins_group.permissions.set(Permission.objects.filter(codename__in=['change_Person', 'view_Person', 'add_Person', 'delete_Person']))


# create student view       
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


# create teacher view
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


# create admin view
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


# edit student attendance view
@api_view(['POST'])
@permission_required('accounts.change_Student')
def edit_student_attendance(request, student_id, session_id):
     # 1. Create Attendance model 
        #
    # 2. Retrieve the student and session objects
        # student = get_object_or_404(Student, id=student_id)
        # session = get_object_or_404(Session, id=session_id)

    # 3. Check if the teacher is assigned to the course of the session
        # if request.user not in session.s_group.g_teacher.all():
        #     return Response({'message': 'Unauthorized'}, status=401)

    # 4. Check if the attendance record for this student and session already exists
        # try:
        #     attendance = Attendance.objects.get(student=student, session=session)
        # except Attendance.DoesNotExist:
        #     attendance = None

    # 5. Update or create the attendance record based on the "is_present" parameter
        # is_present = request.data.get('is_present')
        # if is_present is None:
        #     return Response({'message': 'Missing "is_present" parameter'}, status=400)

        # if attendance is not None:
        #     attendance.is_present = is_present
        #     attendance.save()
        # else:
        #     attendance = Attendance.objects.create(student=student, session=session, is_present=is_present)

    # 6. Return the attendance record
        # 
        # num_attended = attendance.filter(student=student, is_present=True).count()
        # num_missed = attendance.filter(student=student, is_present=False).count()
        # return Response({'message': 'Attendance updated, 'attended': num_attended, 'missed': num_missed}, status=200)
    pass


#view that lists all students
@method_decorator(permission_required('accounts.view_student'), name='get')
class StudentList(generics.ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

# view that retrieves/updates/destroys a student

@method_decorator(permission_required('accounts.change_Person'), name='put')
@method_decorator(permission_required('accounts.view_Person'), name='get')
class StudentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

#view that lists all teachers

@method_decorator(permission_required('accounts.view_student'), name='get')
class TeacherList(generics.ListAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerializer

# view that retrieves/updates/destroys a teacher
@method_decorator(permission_required('accounts.change_Person'), name='put')
@method_decorator(permission_required('accounts.view_Person'), name='get')
class TeacherRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

#view that lists all Admins

@method_decorator(permission_required('accounts.view_Person'), name='get')
class AdminList(generics.ListAPIView):
    queryset=Admin.objects.all()
    serializer_class=AdminSerializer

# view that retrieves/updates/destroys an Admin
@method_decorator(permission_required('accounts.change_Person'), name='put')
@method_decorator(permission_required('accounts.view_Person'), name='get')
class AdminRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
 