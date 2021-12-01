from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserRegisterForm, UserMarkForm, EmployeeRegisterForm,UserUpdateForm, EmployeeUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required


@login_required
def home(request):
    user = User.objects.get(username=request.user)
    if request.user.is_authenticated==False:
        return redirect('register')
    elif request.method == 'POST':
        today = datetime.date.today()
        form = UserMarkForm(request.POST)
        if mark_the_time.objects.filter(user=user).filter(entry_or_departure='Entry').filter(fech__startswith=today).exists()==False:
            form = UserMarkForm(request.POST)
        
            if form.is_valid():
                mark = form.save(commit=False)
                mark.user = request.user
                mark.entry_or_departure='Entry'

                mark.save()

                return redirect('home')
        elif mark_the_time.objects.filter(user=user).filter(entry_or_departure='Departure').filter(fech__startswith=today).exists()==False:
            if form.is_valid():
                mark = form.save(commit=False)
                mark.user = request.user
                mark.entry_or_departure='Departure'

                mark.save()

                return redirect('home')
        elif mark_the_time.objects.filter(user=user).filter(entry_or_departure='Entry').filter(fech__startswith=today).exists() and mark_the_time.objects.filter(user=user).filter(entry_or_departure='Departure').filter(fech__startswith=today).exists():
            form = UserMarkForm()
    else:
        user = User.objects.get(username=request.user)
        if Employee.objects.filter(user=user).exists()==False:
            employee = Employee(user=user)
            employee.save()

        form = UserMarkForm()
    
    
    hours = mark_the_time.objects.all()
    today = datetime.date.today()
    validator = mark_the_time.objects.filter(user=user).filter(entry_or_departure='Entry').filter(fech__startswith=today).exists()
    validator_complete = mark_the_time.objects.filter(user=user).filter(entry_or_departure='Departure').filter(fech__startswith=today).exists()
    context= {
        'form': form, 
        'today': today, 
        'hours': hours,
        'validator' : validator,
        'validator_complete' : validator_complete,
    }
    return render(request, 'dashboard/index.html', context)


def register(request):
    if request.user.is_authenticated==False:
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = UserRegisterForm()
   
        context = {'form' : form}
        return render(request, 'dashboard/register.html', context)

    else:
        return redirect('login')

@login_required
def profile(request, pk):
    user = User.objects.get(pk=pk)
    context= {
        'profile': user,
    }
    return render(request, 'dashboard/profile.html', context)

@login_required
def editProfile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) #llenar el formulario con informacion que ya tiene
        employee_form = EmployeeUpdateForm(request.POST, request.FILES, instance=request.user.employee)

        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            return redirect('home')

    else:
        user_form = UserUpdateForm(instance=request.user)
        employee_form = EmployeeUpdateForm()

    context={
        'user_form' : user_form, 
        'employee_form' : employee_form,
    }
    return render(request, 'dashboard/edit.html', context)

@staff_member_required
def editProfileAdmin(request, username):
    user = User.objects.get(username=username)
    employee = Employee.objects.get(user=user)
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=user) #llenar el formulario con informacion que ya tiene
        employee_form = EmployeeUpdateForm(request.POST, request.FILES, instance=employee.user)
        if user_form.is_valid() and employee_form.is_valid():
            user_form.save()
            employee_form.save()
            return redirect('home')
    else:
        user_form = UserUpdateForm(instance=employee.user)
        employee_form = EmployeeUpdateForm()

    context={
        'user_form' : user_form, 
        'employee_form' : employee_form,
        'user' : user
    }
    return render(request, 'dashboard/edit.html', context)

@login_required
def employee(request):
    employee = Employee.objects.all()
    context = {
        'employee':employee,
    }

    return render(request, 'dashboard/employee.html', context)

@staff_member_required
def addProfile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = EmployeeRegisterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = EmployeeRegisterForm()
   
        context = {'form' : form}
        return render(request, 'dashboard/add.html', context)

    else:
        return redirect('home')
        
@staff_member_required
def deleteProfile(request, pk):
    user = Employee.objects.get(user=pk)
    user.delete()
    return redirect('employee')
