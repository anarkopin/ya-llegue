from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, date
import datetime


class Employee(models.Model):
    #oneToOne hace mencion a la clase User integrada en django de esta manera extendemos la clase para poder agregarle otros campos
    user = models.OneToOneField(User, on_delete=models.CASCADE) #CASCADE HACE REFERENCIA ASI EN CASO SE ETLIMINA EL REGISTRO SE ELIMINA ODOS LOS QUE DEPENDAN DE ESTE (HIJOS)
    dni = models.CharField(max_length=8, null=False, blank=False)
    bio = models.CharField(default="Hola, twitter", max_length=100)
    image = models.ImageField(default='default.png')
    
    def __str__(self):
        return f"Empleado {self.user.username}"


    
                                                
    def mark_day_for_day(self):
        today = datetime.date.today()
        hours = mark_the_time.objects.filter(user=self.user).filter(fech__startswith=today)
        
        for mark in hours:
            if mark.entry_or_departure=='Entry':
                self.hour_entry = mark.hour
            else:
                self.hour_departure = mark.hour
        
        return (self.hour_entry, self.hour_departure)

    def mark_day_exact(self, año,mes,dia):
        today = datetime.date(año,mes,dia)
        hours = mark_the_time.objects.filter(user=self.user).filter(fech__startswith=today)
        
        for mark in hours:
            if mark.entry_or_departure=='Entry':
                self.hour_entry = mark.hour
            else:
                self.hour_departure = mark.hour
        
        return (self.hour_entry, self.hour_departure)


    def timestodelta(self, hour_entry, hour_departure):
        substract = self.todatetime(hour_departure) - self.todatetime(hour_entry)
        return substract

    def todatetime(self, time):
        return datetime.datetime.today().replace(hour=time.hour, minute=time.minute, second=time.second, microsecond=time.microsecond, tzinfo=time.tzinfo)
        
    

MARK_CHOICES = (
    ('Entry', 'Entry'),
    ('Departure', 'Departure'),
)

class mark_the_time(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_mark')
    entry_or_departure = models.CharField(choices=MARK_CHOICES, max_length=25)
    fech = models.DateField(default=datetime.date.today())
    hour = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"Empleado {self.user} {self.entry_or_departure} marco el {self.hour}"
    

    
    
    