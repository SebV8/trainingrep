from django.db import models

# Create your models here.
class Perfil(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lastN = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    fat = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.name, self.lastN)