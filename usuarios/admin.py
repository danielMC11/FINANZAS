from django.contrib import admin
from .models import Usuario


@admin.register(Usuario)
class AdminUsuario(admin.ModelAdmin):
    fields = ['email', 'nombres', 'apellidos', "password"]