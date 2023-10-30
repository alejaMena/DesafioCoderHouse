from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#super usuario alejandra, contraseña coderhouse1
class familia(models.Model):
    Apellido=models.CharField(max_length=50)
    Pareja=models.TextField(blank=True)
    Tiene_hijos=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Apellido