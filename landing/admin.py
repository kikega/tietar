from django.contrib import admin

# Register your models here.
from .models import *

class PeticionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'nombre', 'telefono', 'email', 'consentimiento', 'atendida')
    list_filter = ('atendida',)


admin.site.register(Peticion, PeticionAdmin)