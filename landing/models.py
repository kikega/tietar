from django.db import models

# Create your models here.
class Peticion(models.Model):

    fecha = models.DateField(auto_now=False, auto_now_add=True)
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(max_length=254)
    texto = models.TextField()
    consentimiento = models.BooleanField()
    atendida = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = ("Peticion")
        verbose_name_plural = ("Peticiones")
        ordering = ['fecha', 'telefono']

    def __str__(self):
        return '{}: {} - {}'.format(self.fecha, self.nombre, self.atendida)