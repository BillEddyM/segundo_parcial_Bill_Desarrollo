from django.db import models

# Create your models here.
class Proveedor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    nif = models.CharField(max_length=8)
    direccion = models.CharField(max_length=40)
