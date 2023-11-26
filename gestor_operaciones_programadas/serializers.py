from rest_framework import serializers
from gestor_operaciones.serializers import SerializadorDetalleIngreso, SerializadorDetalleGasto
from gestor_operaciones.models import *
from gestor_operaciones_programadas.models import *


class SerializadorOperacionesProgramadasUsuarioIngreso(serializers.ModelSerializer):
    detalle_ingreso = SerializadorDetalleIngreso(many=False)

    class Meta:
        model = OperacionesUsuarioProgramadas
        fields = ['to_id', 'cantidad', 'etiqueta', 'hora_programada_desde', 'dias', 'detalle_ingreso']

    
    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monto invalido")

    def create(self, validated_data):
        detalle_ingreso_data = validated_data.pop('detalle_ingreso')
        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request').user.u_id)
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        
        operacion_programada = OperacionesUsuarioProgramadas.objects.create(
        cu_id = cu_id,
        to_id = to_id,
        cantidad = validated_data['cantidad'],
        etiqueta = validated_data['etiqueta'],
        hora_programada_desde = validated_data['hora_programada_desde']
        )

        query_set_dias = DiaSemana.objects.filter(d_id__in=validated_data['dias'])
        lst_dias = list(query_set_dias)
        operacion_programada.dias.add(*lst_dias)

        sci_id=SubcategoriasIngreso.objects.get(pk=detalle_ingreso_data['sci_id'])
        DetalleIngresoProgramado.objects.create(
        op_id=operacion_programada,
        sci_id = sci_id
        )
        
        operacion_programada.save()

        return operacion_programada



class SerializadorOperacionesProgramadasUsuarioGasto(serializers.ModelSerializer):
    detalle_gasto = SerializadorDetalleGasto(many=False)

    class Meta:
        model = OperacionesUsuarioProgramadas
        fields = ['to_id', 'cantidad', 'etiqueta', 'fecha_operacion', 'hora_operacion', 'hora_programada_desde', 'dias', 'detalle_gasto']

    
    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monto invalido")

    def create(self, validated_data):
        detalle_gasto_data = validated_data.pop('detalle_gasto')
        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request').user.u_id)
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        
        time1_str = validated_data['hora_programada_desde']
        time2_str = "06:00:00"

        time1 = datetime.datetime.strptime(time1_str, "%H:%M:%S").time()
        time2 = datetime.datetime.strptime(time2_str, "%H:%M:%S").time()

        total_time = time1 + time2
        formatted_total_time = total_time.strftime("%H:%M:%S")


        operacion_programada = OperacionesUsuarioProgramadas.objects.create(
        cu_id = cu_id,
        to_id = to_id,
        cantidad = validated_data['cantidad'],
        etiqueta = validated_data['etiqueta'],
        fecha_operacion = validated_data['fecha_operacion'],
        hora_operacion = validated_data['hora_operacion'],
        hora_programada_desde = validated_data['hora_programada_desde'],
        hora_programada_hasta = formatted_total_time
        )

        query_set_dias = DiaSemana.objects.filter(d_id__in=validated_data['dias'])
        lst_dias = list(query_set_dias)
        operacion_programada.dias.add(*lst_dias)

        scg_id=SubcategoriasGasto.objects.get(pk=detalle_gasto_data['scg_id'])
        DetalleGastoProgramado.objects.create(
        op_id=operacion_programada,
        scg_id = scg_id
        )
        
        operacion_programada.save()

        return operacion_programada
    

class SerializadorExtractos(serializers.ModelSerializer):
    divisa = serializers.CharField(source='cu_id.divisa')
    tipo_operacion = serializers.CharField(source='to_id.nom_to')

    class Meta:
        model = OperacionesUsuarioProgramadas
        fields = ('op_id', 'etiqueta', 'cantidad', 'divisa', 'tipo_operacion', 'fecha_operacion', 'hora_operacion', 'hora_programada_desde')