from django.db import models

# Create your models here.
class Car(models.Model):
    placa = models.CharField(max_length=6)
    duenio = models.CharField(max_length=50)
    modelo =  models.IntegerField(default=0)
    marca = models.CharField(max_length=25, default="")