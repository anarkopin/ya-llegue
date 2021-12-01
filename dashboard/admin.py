from django.contrib import admin
from .models import Employee, mark_the_time

# Register your models here.

admin.site.register(Employee)
admin.site.register(mark_the_time)
