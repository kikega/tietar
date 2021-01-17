from django.contrib import admin

# Register your models here.
from .models import *

class PeticionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nombre', 'telefono', 'email', 'consentimiento', 'atendida')
    list_filter = ('atendida',)


class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nombre', 'descripcion')


admin.site.register(Peticion, PeticionAdmin)
admin.site.register(Galeria_fotos, GaleriaAdmin)