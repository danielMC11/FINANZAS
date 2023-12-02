from django.db import models
from gestor_cartera.models import CarteraUsuario
from gestor_operaciones.models import TipoOperacion, OperacionesUsuario
from gestor_operaciones.utils import fecha_actual, adicion_fecha_actual

class ProyeccionesFinancieras(models.Model):
    pf_id = models.CharField(max_length=20, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.PROTECT, db_column='cu_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    etiqueta = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=fecha_actual)
    fecha_fin = models.DateField(default=adicion_fecha_actual)
    cantidad_proyeccion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad_progreso = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        if not self.pf_id:
            self.pf_id = f"pf{ProyeccionesFinancieras.objects.count() + 1}"
        return super().save(*args, **kwargs)    

    @classmethod
    def progreso_proyeccion(cls, operacion: OperacionesUsuario):
        proyecciones = ProyeccionesFinancieras.objects.filter(cu_id=operacion.cu_id, to_id=operacion.to_id.to_id ,fecha_inicio__lte=operacion.fecha_operacion, fecha_fin__gte=operacion.fecha_operacion)
        if proyecciones:
            for i in proyecciones:
                i.cantidad_progreso += operacion.cantidad
                i.save()
        return
        
    class Meta:
        db_table = 'proyecciones_financieras'


class HistoricoProyeccionesFinancieras(models.Model):
    hpf_id = models.CharField(max_length=20, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.PROTECT, db_column='op_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    etiqueta = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True)
    fecha_fin = models.DateField(null=True)
    cantidad_proyeccion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def save(self, *args, **kwargs):
        if not self.hpf_id:
            self.hpf_id = f"hpf{HistoricoProyeccionesFinancieras.objects.count() + 1}"
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'historico_proyecciones_financieras'
        
        