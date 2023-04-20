from django.db import models
import datetime

class Enlace(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    image = models.ImageField(upload_to="static/img")
    url = models.URLField(blank=True)
    date = models.DateField(datetime.date.today)
    
