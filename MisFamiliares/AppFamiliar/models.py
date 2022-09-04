from django.db import models

# Create your models here.
class familia(models,model):
    nombre=models.CharField(max_lenght=50)
    apellido=models.CharField(max_lenght=50)
    edad=models.IntegerField()
    fecha=models.DateField()
