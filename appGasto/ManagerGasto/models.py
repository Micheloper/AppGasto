from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Activo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    proposito = models.CharField(max_length=100)
    importe_Total = models.DecimalField(max_digits=100000,decimal_places=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.proposito
    
class Costo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    activo = models.ForeignKey(Activo,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=100)
    importe = models.DecimalField(max_digits=100000,decimal_places=1)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.descripcion
    