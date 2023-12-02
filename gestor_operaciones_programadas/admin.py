from django.contrib import admin
from .models import OperacionesUsuarioProgramadas, DetalleGastoProgramado, DetalleIngresoProgramado


class DetalleIngresoProgramadoInline(admin.StackedInline):
    exclude = ['dip_id']
    model = DetalleIngresoProgramado

class DetalleGastoProgramadoInline(admin.StackedInline):
    exclude = ['dgp_id']
    model = DetalleGastoProgramado

@admin.register(OperacionesUsuarioProgramadas)
class OperacionesProgramadasAdmin(admin.ModelAdmin):
    exclude = ['op_id']
    inlines = (DetalleIngresoProgramadoInline, DetalleGastoProgramadoInline)