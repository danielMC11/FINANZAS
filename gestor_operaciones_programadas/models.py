from django.db import models
from gestor_cartera.models import CarteraUsuario
from gestor_operaciones.models import TipoOperacion, SubcategoriasGasto, SubcategoriasIngreso
from django.utils import timezone
import datetime

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
    fecha_operacion = models.DateField(default=timezone.localtime(timezone.now(), timezone.get_fixed_timezone(-300) ).replace(microsecond=0))
    hora_operacion = models.TimeField(default=timezone.localtime(timezone.now(), timezone.get_fixed_timezone(-300) ).time().replace(microsecond=0))
    hora_programada_desde = models.TimeField()# default=timezone.localtime(timezone.now(), timezone.get_fixed_timezone(-300) ).time().replace(microsecond=0))
    hora_programada_hasta = models.TimeField()# default=(datetime.datetime.combine(datetime.date.today(), timezone.localtime(timezone.now(), timezone.get_fixed_timezone(-300) ).time().replace(microsecond=0)) + datetime.timedelta(hours=6)).time())
    dias = models.ManyToManyField(DiaSemana)
    activo = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.op_id:
            self.op_id = f"op{OperacionesUsuarioProgramadas.objects.count() + 1}"
        return super().save(*args, **kwargs)
    
    @classmethod
    def extractos_operaciones(cls, u_id):
        cartera=CarteraUsuario.objects.get(u_id=u_id)
        extractos = OperacionesUsuarioProgramadas.objects.filter(cu_id=cartera.cu_id)
        return extractos

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