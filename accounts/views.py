from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.groups.filter(name__in=['admins', 'superUsers']).exists())
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
    
    # Add the user to the teacher group
    teacher_group = Group.objects.get(name='teachers')
    teacher_group.user_set.add(user)

    # Return a success message
    return JsonResponse({'success': True})

@user_passes_test(lambda u: u.groups.filter(name='superUsers').exists())
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

    # Add the user to the superuser group
    superuser_group = Group.objects.get(name='superusers')
    superuser_group.user_set.add(user)

    # Return a success message
    return JsonResponse({'success': True})

@user_passes_test(lambda u: u.groups.filter(name='superUsers').exists())
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

    # Add the user to the admin group
    admin_group = Group.objects.get(name='admins')
    admin_group.user_set.add(user)

    # Return a success message
    return JsonResponse({'success': True})


@user_passes_test(lambda u: u.groups.filter(name='teachers').exists())
def edit_student_attendance(request, student_id):
    # modifier l'absence et la presence des etudiants
    # il faut voir qvel es que l'etudiant ni n le group ines negh khati
    #...
    return JsonResponse({'success': True})