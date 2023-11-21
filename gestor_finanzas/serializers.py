from rest_framework import serializers
from .models import *

class SerializadorCarteraUsuario(serializers.ModelSerializer):
    class Meta:
        model = CarteraUsuario
        fields = ["saldo", "divisa"]

    def validate_saldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("Saldo invalido")
        
    def create(self, validated_data):
        user = CarteraUsuario.objects.create(
            u_id=Usuario.objects.get(pk=self.context.get('request').user.u_id),
            saldo=validated_data['saldo'],
            divisa=validated_data['divisa'])
        user.save()
        return user



class SerializadorDetalleIngreso(serializers.ModelSerializer):
    class Meta:
        model = DetalleIngreso
        fields = ['etiqueta', 'sci_id']


class SerializadorOperacionesUsuarioIngreso(serializers.ModelSerializer):
    detalle_ingreso = SerializadorDetalleIngreso(many=False)

    class Meta:
        model = OperacionesUsuario
        fields = ['to_id', 'cantidad', 'detalle_ingreso']

    
    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monto invalido")

    def create(self, validated_data):
        detalle_ingreso_data = validated_data.pop('detalle_ingreso')
        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request').user.u_id)
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        operacion = OperacionesUsuario.objects.create(
        cu_id = cu_id,
        to_id = to_id,
        cantidad = validated_data['cantidad'],
        )

        cu_id.saldo += validated_data['cantidad']
        cu_id.save()

        sci_id=SubcategoriasIngreso.objects.get(pk=detalle_ingreso_data['sci_id'])
        DetalleIngreso.objects.create(
        o_id=operacion,
        etiqueta = detalle_ingreso_data['etiqueta'],
        sci_id = sci_id
        )
        
        operacion.save()

        return operacion
    

class SerializadorDetalleGasto(serializers.ModelSerializer):
    class Meta:
        model = DetalleGasto
        fields = ['etiqueta', 'scg_id']

class SerializadorOperacionesUsuarioGasto(serializers.ModelSerializer):
    detalle_gasto = SerializadorDetalleGasto(many=False)

    class Meta:
        model = OperacionesUsuario
        fields = ['to_id', 'cantidad', 'detalle_gasto']

    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monto invalido")
        cartera=CarteraUsuario.objects.get(u_id=self.context.get('request').user.u_id)
        if value > cartera.saldo:
            raise serializers.ValidationError("Fondos insuficientes")
        return value
    
    def create(self, validated_data):
        detalle_gasto_data = validated_data.pop('detalle_gasto')
        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request').user.u_id)
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        operacion = OperacionesUsuario.objects.create(
        cu_id = cu_id,
        to_id = to_id,
        cantidad = validated_data['cantidad'],
        )

        cu_id.saldo -= validated_data['cantidad']
        cu_id.save()

        scg_id=SubcategoriasGasto.objects.get(pk=detalle_gasto_data['scg_id'])
        DetalleGasto.objects.create(
        o_id=operacion,
        etiqueta = detalle_gasto_data['etiqueta'],
        scg_id = scg_id
        )

        operacion.save()

        return operacion
    
