from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

class CarteraUsuario(models.Model):
    cu_id = models.CharField(max_length=10, primary_key=True)
    u_id = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    saldo = models.FloatField
    divisa = models.CharField(max_length=3)

class CategoriasGasto(models.Model):
    cg_id = models.CharField(max_length=10, primary_key=True)
    nom_cg = models.CharField(max_length=20)

class SubcategoriasGasto(models.Model):
    scg_id = models.CharField(max_length=10, primary_key=True)
    nom_scg = models.CharField(max_length=20)
    cg_id = models.ForeignKey(CategoriasGasto, on_delete=models.PROTECT)

class CategoriasIngreso(models.Model):
    ci_id = models.CharField(max_length=10, primary_key=True)
    nom_ci = models.CharField(max_length=20)

class SubcategoriasIngreso(models.Model):
    sci_id = models.CharField(max_length=10, primary_key=True)
    nom_sci = models.CharField(max_length=20)
    ci_id = models.ForeignKey(CategoriasIngreso, on_delete=models.PROTECT)

class DetalleGasto(models.Model):
    dg_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField("OperacionesUsuario", on_delete=models.PROTECT)
    etiqueta = models.CharField(max_length=30)
    subsidiado = models.BooleanField(default=False)
    scg_id = models.ForeignKey(SubcategoriasGasto, on_delete=models.PROTECT)

class DetalleIngreso(models.Model):
    di_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField("OperacionesUsuario", on_delete=models.PROTECT)
    etiqueta = models.CharField(max_length=30)
    sci_id = models.ForeignKey(SubcategoriasIngreso, on_delete=models.PROTECT)

class TipoOperacion(models.Model):
    to_id = models.CharField(max_length=3, primary_key=True)
    nom_to = models.CharField(max_length=10)

class OperacionesUsuario(models.Model):
    o_id = models.CharField(max_length=10, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.CASCADE)
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT)
    cantidad = models.FloatField
    fecha = models.DateTimeField(default=timezone.now())

class DetalleGastoProgramado(models.Model):
    dgp_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField("OperacionesUsuarioProgramadas", on_delete=models.PROTECT)
    etiqueta = models.CharField(max_length=30)
    subsidiado = models.BooleanField(default=False)
    scg_id = models.ForeignKey(SubcategoriasGasto, on_delete=models.PROTECT)

class DetalleIngresoProgramado(models.Model):
    dip_id = models.CharField(max_length=10, primary_key=True)
    op_id = models.OneToOneField("OperacionesUsuarioProgramadas", on_delete=models.PROTECT)
    etiqueta = models.CharField(max_length=30)
    sci_id = models.ForeignKey(SubcategoriasIngreso, on_delete=models.PROTECT)

class OperacionesUsuarioProgramadas(models.Model):

    LUNES = 'Monday'
    MARTES = 'Tuesday'
    MIERCOLES = 'Wednesday'
    JUEVES = 'Thursday'
    VIERNES = 'Friday'
    SABADO = 'Saturday'
    DOMINGO = 'Sunday'

    DIAS_DE_LA_SEMANA = [
        (LUNES, 'Monday'),
        (MARTES, 'Tuesday'),
        (MIERCOLES, 'Wednesday'),
        (JUEVES, 'Thursday'),
        (VIERNES, 'Friday'),
        (SABADO, 'Saturday'),
        (DOMINGO, 'Sunday'),
    ]


    op_id = models.CharField(max_length=10, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.CASCADE)
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT)
    cantidad = models.FloatField
    fecha = models.DateTimeField(default=timezone.now())

    dia = models.TextField(choices=DIAS_DE_LA_SEMANA)
    hora = models.TimeField
    activo = models.BooleanField(default=True)

class PlanesGasto(models.Model):
    pg_id = models.CharField(max_length=20, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.CASCADE)
    etiqueta = models.CharField(max_length=30)
    cantidad = models.FloatField
    cg_id = models.ForeignKey(CategoriasGasto, on_delete=models.PROTECT)
    fecha_inicio = models.DateField
    fecha_fin = models.DateField
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)

class HistoricoPlanesGasto(models.Model):
    hpg_id = models.CharField(max_length=20, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.CASCADE)
    etiqueta = models.CharField(max_length=30)
    cg_id = models.ForeignKey(CategoriasGasto, on_delete=models.PROTECT)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    exito = models.BooleanField     
