from django.contrib import admin
from .models import OperacionesUsuario, DetalleGasto, SubcategoriasGasto, DetalleIngreso, CarteraUsuario


class DetalleIngresoInline(admin.StackedInline):
    exclude = ['di_id']
    model = DetalleIngreso

class DetalleGastoInline(admin.StackedInline):
    exclude = ['dg_id']
    model = DetalleGasto


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



admin.site.register(OperacionesUsuario, OperacionesAdmin)


class CarteraAdmin(admin.ModelAdmin):
    exclude = ['cu_id']

admin.site.register(CarteraUsuario, CarteraAdmin)
