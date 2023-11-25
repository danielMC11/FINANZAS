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

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        cantidad = form.cleaned_data.get('cantidad')  
        cartera = obj.cu_id
        operacion = str(form.cleaned_data.get('to_id'))
        if operacion == 'ingreso': 
            cartera.saldo += cantidad
        elif operacion == 'gasto':
            cartera.saldo -= cantidad
        cartera.save()