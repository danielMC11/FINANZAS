from django.contrib import admin
from gestor_proyecciones.models import ProyeccionesFinancieras

@admin.register(ProyeccionesFinancieras)
class ProyeccionesFinancierasAdmin(admin.ModelAdmin):
    exclude = ['pf_id', 'cantidad_progreso']
