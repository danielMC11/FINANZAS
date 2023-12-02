from django.db import models
from gestor_cartera.models import CarteraUsuario
from gestor_operaciones.models import TipoOperacion, SubcategoriasGasto, SubcategoriasIngreso
from gestor_operaciones.utils import dia_semana_actual, fecha_actual, hora_actual, adicion_hora_actual
from django.utils import timezone
from datetime import datetime, timedelta

class DiaSemana(models.Model):
    d_id = models.CharField(max_length=10, primary_key=True)
    nom_dia = models.CharField(max_length=30)

    class Meta:
        db_table = 'dia_semana'

class OperacionesUsuarioProgramadas(models.Model):
    op_id = models.CharField(max_length=10, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.PROTECT, db_column='cu_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    etiqueta = models.CharField(max_length=50, default='')
    fecha_operacion = models.DateField(default=fecha_actual)
    hora_operacion = models.TimeField(default=hora_actual)
    hora_programada_desde = models.TimeField(default=hora_actual)
    hora_programada_hasta = models.TimeField(default=adicion_hora_actual)
    dias = models.ManyToManyField(DiaSemana)
    activo = models.BooleanField(default=True)
    
    def save(self, *args, **kwargs):
        if not self.op_id:
            self.op_id = f"op{OperacionesUsuarioProgramadas.objects.count() + 1}"
        return super().save(*args, **kwargs)
    
    @classmethod
    def operaciones_programadas(cls, u_id):
        cartera=CarteraUsuario.objects.get(u_id=u_id)
        extractos = OperacionesUsuarioProgramadas.objects.filter(cu_id=cartera.cu_id)
        return extractos
    
    @classmethod
    def operaciones_habilitadas(cls, u_id):
        cartera=CarteraUsuario.objects.get(u_id=u_id)
        n_dia_actual = dia_semana_actual()
        d_id = f'd{n_dia_actual}'
        qset_lst = OperacionesUsuarioProgramadas.objects.filter(cu_id=cartera.cu_id, dias=d_id, hora_programada_desde__lte=hora_actual(), hora_programada_hasta__gte=hora_actual())
        return qset_lst
    
    @classmethod
    def operacion_info(cls, op_id):
        operacion_programada = OperacionesUsuarioProgramadas.objects.get(op_id=op_id)
        if operacion_programada.to_id.nom_to == 'ingreso':
            dict_registro = {
            "to_id": operacion_programada.to_id.to_id,
            "cantidad": operacion_programada.cantidad,
            "etiqueta": operacion_programada.etiqueta,
            "detalle_ingreso":{
            "sci_id": operacion_programada.detalleingresoprogramado.sci_id.sci_id
            }
            }
            return dict_registro
        else:
            dict_registro = {
            "to_id": operacion_programada.to_id.to_id,
            "cantidad": operacion_programada.cantidad,
            "etiqueta": operacion_programada.etiqueta,
            "detalle_gasto":{
            "scg_id": operacion_programada.detallegastoprogramado.scg_id.scg_id
            }
            }
            return dict_registro


    class Meta:
        db_table = 'operaciones_usuario_programadas'

    

class DetalleGastoProgramado(models.Model):
    dgp_id = models.CharField(max_length=10, primary_key=True)
    op_id = models.OneToOneField(OperacionesUsuarioProgramadas, on_delete=models.PROTECT, db_column='op_id')
    scg_id = models.ForeignKey(SubcategoriasGasto, on_delete=models.PROTECT, db_column='scg_id')

    def save(self, *args, **kwargs):
        if not self.dgp_id:
            self.dgp_id = f"dgp{DetalleGastoProgramado.objects.count() + 1}"
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'detalle_gasto_programado'

class DetalleIngresoProgramado(models.Model):
    dip_id = models.CharField(max_length=10, primary_key=True)
    op_id = models.OneToOneField(OperacionesUsuarioProgramadas, on_delete=models.PROTECT, db_column='op_id')
    sci_id = models.ForeignKey(SubcategoriasIngreso, on_delete=models.PROTECT, db_column='sci_id')

    def save(self, *args, **kwargs):
        if not self.dip_id:
            self.dip_id = f"dip{DetalleIngresoProgramado.objects.count() + 1}"
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'detalle_ingreso_programado'