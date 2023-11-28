from rest_framework import serializers
from gestor_operaciones.serializers import SerializadorDetalleIngreso, SerializadorDetalleGasto
from gestor_operaciones.models import *
from gestor_operaciones_programadas.models import *
from datetime import timedelta

class SerializadorOperacionesProgramadasUsuarioIngreso(serializers.ModelSerializer):
    detalle_ingreso = SerializadorDetalleIngreso(many=False)
    hora_operacion = serializers.TimeField(required=False)
    fecha_operacion = serializers.DateField(required=False)

    class Meta:
        model = OperacionesUsuarioProgramadas
        fields = ['to_id', 'cantidad', 'etiqueta', 'fecha_operacion', 'hora_operacion', 'hora_programada_desde', 'dias', 'detalle_ingreso']

    
    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monto invalido")

    def create(self, validated_data):
        detalle_ingreso_data = validated_data.pop('detalle_ingreso')
        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request'))
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])
        
        hora_operacion = validated_data.get('hora_operacion', None)
        fecha_operacion = validated_data.get('fecha_operacion', None)
        operacion_programada = None

        if fecha_operacion and hora_operacion:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            fecha_operacion = validated_data['fecha_operacion'],
            hora_operacion = validated_data['hora_operacion'],
            hora_programada_desde =validated_data['hora_programada_desde']

            )
        elif fecha_operacion and not hora_operacion:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            fecha_operacion = validated_data['fecha_operacion'],
            hora_programada_desde =validated_data['hora_programada_desde']
            )
        elif not fecha_operacion and hora_operacion:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            hora_operacion = validated_data['hora_operacion'],
            hora_programada_desde =validated_data['hora_programada_desde']
            )
        else:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            hora_programada_desde =validated_data['hora_programada_desde']
            )

        lst = validated_data['hora_programada_desde'].split(':')
        lst = [int(i) for i in lst]
        h, m, s = lst

        total_time = timedelta(hours=h, minutes=m, seconds=s) + timedelta(hours=6, minutes=0, seconds=0)

        total_seconds = total_time.total_seconds() - total_time.days*86400

        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        operacion_programada.hora_programada_hasta = f'{int(hours)}:{int(minutes)}:{int(seconds)}'

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
    hora_operacion = serializers.TimeField(required=False)
    fecha_operacion = serializers.DateField(required=False)

    class Meta:
        model = OperacionesUsuarioProgramadas
        fields = ['to_id', 'cantidad', 'etiqueta', 'fecha_operacion', 'hora_operacion', 'hora_programada_desde', 'dias', 'detalle_gasto']

    
    def validate_cantidad(self, value):
        if value <= 0:
            raise serializers.ValidationError("Monto invalido")

    def create(self, validated_data):
        detalle_gasto_data = validated_data.pop('detalle_gasto')
        cu_id=CarteraUsuario.objects.get(u_id=self.context.get('request'))
        to_id=TipoOperacion.objects.get(pk=validated_data['to_id'])

        hora_operacion = validated_data.get('hora_operacion', None)
        fecha_operacion = validated_data.get('fecha_operacion', None)
        operacion_programada = None

        if fecha_operacion and hora_operacion:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            fecha_operacion = validated_data['fecha_operacion'],
            hora_operacion = validated_data['hora_operacion'],
            hora_programada_desde =validated_data['hora_programada_desde']

            )
        elif fecha_operacion and not hora_operacion:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            fecha_operacion = validated_data['fecha_operacion'],
            hora_programada_desde =validated_data['hora_programada_desde']
            )
        elif not fecha_operacion and hora_operacion:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            hora_operacion = validated_data['hora_operacion'],
            hora_programada_desde =validated_data['hora_programada_desde']
            )
        else:
            operacion_programada = OperacionesUsuarioProgramadas.objects.create(
            cu_id = cu_id,
            to_id = to_id,
            etiqueta = validated_data['etiqueta'],
            cantidad = validated_data['cantidad'],
            hora_programada_desde =validated_data['hora_programada_desde']
            )

        lst = validated_data['hora_programada_desde'].split(':')
        lst = [int(i) for i in lst]
        h, m, s = lst
    
        total_time = timedelta(hours=h, minutes=m, seconds=s) + timedelta(hours=6, minutes=0, seconds=0)

        total_seconds = total_time.total_seconds() - total_time.days*86400
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        operacion_programada.hora_programada_hasta = f'{int(hours)}:{int(minutes)}:{int(seconds)}'
    
        query_set_dias = DiaSemana.objects.filter(d_id__in=validated_data['dias'])
        lst_dias = list(query_set_dias)
        operacion_programada.dias.add(*lst_dias)


        operacion_programada.save()


        scg_id=SubcategoriasGasto.objects.get(pk=detalle_gasto_data['scg_id'])
        DetalleGastoProgramado.objects.create(
        op_id=operacion_programada,
        scg_id = scg_id
        )
        
        return operacion_programada
    

class SerializadorOperacionesHabilitadas(serializers.ModelSerializer):
    divisa = serializers.CharField(source='cu_id.divisa')
    tipo_operacion = serializers.CharField(source='to_id.nom_to')

    class Meta:
        model = OperacionesUsuarioProgramadas
        fields = ('op_id', 'etiqueta', 'cantidad', 'divisa', 'tipo_operacion', 'fecha_operacion', 'hora_operacion', 'hora_programada_desde')