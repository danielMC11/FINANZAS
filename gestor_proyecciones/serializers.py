from rest_framework import serializers
from gestor_proyecciones.models import *
from gestor_cartera.models import CarteraUsuario
#from gestor_operaciones.utils import validar_fechas
from django.core.exceptions import ValidationError

class SerializadorProyecciones(serializers.ModelSerializer):

    class Meta:
        model = ProyeccionesFinancieras
        fields = ['to_id', 'etiqueta', 'fecha_inicio', 'fecha_fin', 'cantidad_proyeccion']

    def create(self, validated_data):

        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request'))
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
    
        proyeccion = ProyeccionesFinancieras.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            fecha_inicio = validated_data['fecha_inicio'],
            fecha_fin = validated_data['fecha_fin'],
            cantidad_proyeccion = validated_data['cantidad_proyeccion']
        )

        proyeccion.save()

        return proyeccion








"""
    def validate(self, data):
            if data['cantidad_proyeccion'] <= 0:
                raise ValidationError('monto invalido')
            if not validar_fechas(data['fecha_inicio'], data['fecha_fin']):
                raise ValidationError('La fecha inicial no puede ser mayor a la final')
"""
    