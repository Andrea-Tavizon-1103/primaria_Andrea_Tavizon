from django.db import models

# Create your models here.

class Alumno(models.Model):
    apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno jajaj")
    amaterno=models.CharField(max_length=50, verbose_name="Apellido Materno")
    nombre=models.CharField(max_length=100,verbose_name="Nombre (s)")
    fecha_nac=models.DateField(verbose_name="Fecha de Nacimiento", null=False,blank=False)
    fecha_ing=models.DateField(verbose_name="Fecha de Ingreso", null=False,blank=False)

