from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class SerializadorDetalleIngreso(serializers.ModelSerializer):
    class Meta:
        model = DetalleIngreso
        fields = ['sci_id']


class SerializadorOperacionesUsuarioIngreso(serializers.ModelSerializer):
    detalle_ingreso = SerializadorDetalleIngreso(many=False)

    class Meta:
        model = OperacionesUsuario
        fields = ['to_id', 'cantidad', 'etiqueta', 'fecha_operacion', 'hora_operacion', 'detalle_ingreso']

    
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
        etiqueta = validated_data['etiqueta'],
        cantidad = validated_data['cantidad'],
        fecha_operacion = validated_data['fecha_operacion'],
        hora_operacion = validated_data['hora_operacion']
        )

        cu_id.saldo += validated_data['cantidad']
        cu_id.save()

        sci_id=SubcategoriasIngreso.objects.get(pk=detalle_ingreso_data['sci_id'])
        DetalleIngreso.objects.create(
        o_id=operacion,
        sci_id = sci_id
        )
        
        operacion.save()

        return operacion
    

class SerializadorDetalleGasto(serializers.ModelSerializer):
    class Meta:
        model = DetalleGasto
        fields = ['scg_id']

class SerializadorOperacionesUsuarioGasto(serializers.ModelSerializer):
    detalle_gasto = SerializadorDetalleGasto(many=False)

    class Meta:
        model = OperacionesUsuario
        fields = ['to_id', 'cantidad', 'etiqueta', 'detalle_gasto']

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
        etiqueta = validated_data['etiqueta'],
        cantidad = validated_data['cantidad'],
        )

        cu_id.saldo -= validated_data['cantidad']
        cu_id.save()

        scg_id=SubcategoriasGasto.objects.get(pk=detalle_gasto_data['scg_id'])
        DetalleGasto.objects.create(
        o_id=operacion,
        scg_id = scg_id
        )

        operacion.save()

        return operacion

class SerializadorExtractos(serializers.ModelSerializer):
    divisa = serializers.CharField(source='cu_id.divisa')
    tipo_operacion = serializers.CharField(source='to_id.nom_to')

    class Meta:
        model = OperacionesUsuario
        fields = ('o_id', 'etiqueta', 'cantidad', 'divisa', 'tipo_operacion', 'fecha_operacion', 'hora_operacion')

class SerializadorExtractoDetalleIngreso(serializers.ModelSerializer):

    tipo_operacion = serializers.CharField(max_length=30, source='to_id.nom_to')
    subcategoria_ingreso = serializers.CharField(max_length=5, source='detalleingreso.sci_id.nom_sci')
    categoria_ingreso = serializers.CharField(max_length=50, source='detalleingreso.sci_id.ci_id.nom_ci')
    divisa = serializers.CharField(max_length=3, source='cu_id.divisa')

    class Meta:
        model = OperacionesUsuario
        fields = ('o_id', 'cantidad', 'tipo_operacion', 'etiqueta', 'subcategoria_ingreso', 'categoria_ingreso', 'divisa', 'fecha_operacion', 'hora_operacion')


class SerializadorExtractoDetalleGasto(serializers.ModelSerializer):

    tipo_operacion = serializers.CharField(max_length=30, source='to_id.nom_to')
    subcategoria_gasto = serializers.CharField(max_length=5, source='detallegasto.scg_id.nom_scg')
    categoria_gasto = serializers.CharField(max_length=50, source='detallegasto.scg_id.cg_id.nom_cg')
    divisa = serializers.CharField(max_length=3, source='cu_id.divisa')

    class Meta:
        model = OperacionesUsuario
        fields = ('o_id', 'cantidad', 'tipo_operacion', 'etiqueta', 'subcategoria_gasto', 'categoria_gasto', 'divisa', 'fecha_operacion', 'hora_operacion')


