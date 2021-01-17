from django.db import models

# Create your models here.
class Peticion(models.Model):
    """Tabla que a a almacenar los datos recibidos en el formulario de contacto"""
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    nombre = models.CharField(max_length=80)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(max_length=254)
    texto = models.TextField()
    emailcomercial = models.BooleanField(default=False)
    consentimiento = models.BooleanField()
    atendida = models.BooleanField(default=False)
    

    class Meta:
        verbose_name = ("Peticion")
        verbose_name_plural = ("Peticiones")
        ordering = ['fecha', 'telefono']

    def __str__(self):
        return '{}: {} - {}'.format(self.fecha, self.nombre, self.atendida)


class Galeria_fotos(models.Model):
    """Tabla que almacena las fotos subidas"""
    fecha = models.DateField(auto_now=False, auto_now_add=True)
    imagen = models.ImageField(upload_to='fotos')
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()

    class Meta:
        ordering = ['-fecha']

    def __str__(self):
        return '{} {}'.format(self.fecha, self.nombre)