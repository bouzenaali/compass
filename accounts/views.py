from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.models import Permission
from django.contrib.auth.decorators import permission_required

@permission_required('accounts.add_Person')
def create_student(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('mail')
    password = request.POST.get('password')

    # Check if the user already exists
    if User.objects.filter(username=name).exists:
        return JsonResponse({'success':False, 'message': 'User already exists'})
    
    # Create the User object
    user = User.objects.create_user(username=name, password=password)
    user.is_staff = False 
    user.is_superuser = False 
    user.save()

    # add user role
    user.role = User.STUDENT
    user.save()


    # Return a success message
    return JsonResponse({'success': True})


@permission_required('accounts.add_Person')
def create_teacher(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('mail')
    password = request.POST.get('password')

    # Check if the user already exists
    if User.objects.filter(username=name).exists:
        return JsonResponse({'success':False, 'message': 'User already exists'})
    
    # Create the User object
    user = User.objects.create_user(username=name, password=password)
    user.is_staff = False 
    user.is_superuser = False 
    user.save()
    
    # add default permissions to each user created
    permissions = Permission.objects.filter(codename__in=['change_Student', 'view_Student'])
    user.user_permissions.set(permissions)
    user.save()

    # add user role
    user.role = User.TEACHER
    user.save()

    # Return a success message
    return JsonResponse({'success': True})


def create_superUser(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('mail')
    password = request.POST.get('password')

    # Check if the user already exists
    if User.objects.filter(username=name).exists:
        return JsonResponse({'success':False, 'message': 'User already exists'})
    
    # Create the User object
    user = User.objects.create_user(username=name, password=password)
    user.is_staff = True 
    user.is_superuser = True 
    user.save()

    # add user role
    user.role = User.SUPERUSER
    user.save()


    # Return a success message
    return JsonResponse({'success': True})

@permission_required('accounts.add_Person')
def create_admin(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('mail')
    password = request.POST.get('password')

    # Check if the user already exists
    if User.objects.filter(username=name).exists:
        return JsonResponse({'success':False, 'message': 'User already exists'})
       
    # Create the User object
    user = User.objects.create_user(username=name, password=password)
    user.is_staff = True 
    user.is_superuser = False 
    user.save()

    # add default permissions to each user created
    permissions = Permission.objects.filter(codename__in=['add_Person', 'change_Person', 'delete_Person', 'view_Person'])
    user.user_permissions.set(permissions)
    user.save()

    # add user role
    user.role = User.ADMIN
    user.save()

    # Return a success message
    return JsonResponse({'success': True})

@permission_required('accounts.change_Student')
def edit_student_attendance(request, student_id):
    # modifier l'absence et la presence des etudiants
    # il faut voir qvel es que l'etudiant ni n le group ines negh khati
    #...
    return JsonResponse({'success': True})