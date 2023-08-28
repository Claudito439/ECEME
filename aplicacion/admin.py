from django.contrib import admin
from .models import Pais, Fuerza, Regimiento

@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'abreviacion')

@admin.register(Fuerza)
class FuerzaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais')

@admin.register(Regimiento)
class RegimientoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fuerza')