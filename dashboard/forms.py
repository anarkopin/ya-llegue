from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password1', 'password2']

class EmployeeRegisterForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['image', 'dni', 'user']

    
class UserMarkForm(forms.ModelForm): 
    def __init__(self, *args, **kwargs):                            #constructor para que un campo de formulario sea de solo lectura
       super(UserMarkForm, self).__init__(*args, **kwargs)
       self.fields['hour'].widget.attrs['readonly'] = True

    class Meta:
        model = mark_the_time   #modelo que queremos usar
        fields = ['hour'] 

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User   #modelo que queremos usar
        fields = ['first_name', 'username']   #campos del modelo que queremos editar
         
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['image','bio']