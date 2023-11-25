from django.contrib import admin
from .models import CarteraUsuario



@admin.register(CarteraUsuario)
class CarteraAdmin(admin.ModelAdmin):
    exclude = ['cu_id']