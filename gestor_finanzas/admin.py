"""from django.contrib import admin
from .models import CarteraUsuario, OperacionesUsuario, DetalleGasto, DetalleIngreso, OperacionesUsuarioProgramadas, DetalleGastoProgramado, DetalleIngresoProgramado


@admin.register(CarteraUsuario)
class CarteraAdmin(admin.ModelAdmin):
    exclude = ['cu_id']

class DetalleIngresoInline(admin.StackedInline):
    exclude = ['di_id']
    model = DetalleIngreso

class DetalleGastoInline(admin.StackedInline):
    exclude = ['dg_id']
    model = DetalleGasto

@admin.register(OperacionesUsuario)
class OperacionesAdmin(admin.ModelAdmin):
    exclude = ['o_id']
    inlines = (DetalleGastoInline, DetalleIngresoInline)

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
"""