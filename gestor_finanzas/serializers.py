from rest_framework import serializers
from .models import *

class SerializadorCarteraUsuario(serializers.ModelSerializer):
    class Meta:
        model = CarteraUsuario
        fields = ["cu_id", "saldo", "divisa"]

    def create(self, validated_data, u_id):
        user = CarteraUsuario.objects.create(
            cu_id=validated_data['cu_id'], 
            u_id=Usuario.objects.get(pk=u_id),
            saldo=validated_data['saldo'],
            divisa=validated_data['divisa'])
        user.save()
        return user



class SerializadorDetalleIngreso(serializers.ModelSerializer):
    class Meta:
        model = DetalleIngreso
        fields = ['di_id', 'etiqueta', 'sci_id']


class SerializadorOperacionesUsuarioIngreso(serializers.ModelSerializer):
    detalle_ingreso = SerializadorDetalleIngreso(many=False)

    class Meta:
        model = OperacionesUsuario
        fields = ['o_id', 'to_id', 'cantidad', 'detalle_ingreso']

    def create(self, validated_data, u_id):
        detalle_ingreso_data = validated_data.pop('detalle_ingreso')
        cu_id=CarteraUsuario.objects.get(u_id=u_id)
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        operacion = OperacionesUsuario.objects.create(
        o_id = validated_data['o_id'],
        cu_id = cu_id,
        to_id = to_id,
        cantidad = validated_data['cantidad'],
        )

        sci_id=SubcategoriasIngreso.objects.get(pk=detalle_ingreso_data['sci_id'])
        DetalleIngreso.objects.create(
        di_id=detalle_ingreso_data['di_id'],
        o_id=operacion,
        etiqueta = detalle_ingreso_data['etiqueta'],
        sci_id = sci_id
        )
        
        operacion.save()

        return operacion
    

class SerializadorDetalleGasto(serializers.ModelSerializer):
    class Meta:
        model = DetalleGasto
        fields = ['dg_id', 'etiqueta', 'scg_id']

class SerializadorOperacionesUsuarioGasto(serializers.ModelSerializer):
    detalle_gasto = SerializadorDetalleGasto(many=False)

    class Meta:
        model = OperacionesUsuario
        fields = ['o_id', 'to_id', 'cantidad', 'detalle_gasto']

    def create(self, validated_data, u_id):
        detalle_gasto_data = validated_data.pop('detalle_gasto')
        cu_id=CarteraUsuario.objects.get(u_id=u_id)
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        operacion = OperacionesUsuario.objects.create(
        o_id = validated_data['o_id'],
        cu_id = cu_id,
        to_id = to_id,
        cantidad = validated_data['cantidad'],
        )

        scg_id=SubcategoriasGasto.objects.get(pk=detalle_gasto_data['scg_id'])
        DetalleGasto.objects.create(
        dg_id=detalle_gasto_data['dg_id'],
        o_id=operacion,
        etiqueta = detalle_gasto_data['etiqueta'],
        scg_id = scg_id
        )

        operacion.save()

        return operacion
    
