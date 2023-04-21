from django.db import models
from django.contrib.auth.models import User
import datetime

class Enlace(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.URLField(blank=True)
    url = models.URLField(blank=True)
    date = models.DateField(datetime.date.today)
    
class MyUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Agrega aquí cualquier otro campo adicional que desees para tu usuario

    def __str__(self):
        return self.user.username
    
