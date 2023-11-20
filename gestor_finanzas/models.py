from django.db import models
from usuarios.models import Usuario
from django.utils import timezone

class CarteraUsuario(models.Model):
    cu_id = models.CharField(max_length=10, primary_key=True)
    u_id = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='u_id')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    divisa = models.CharField(max_length=3)

    class Meta:
        db_table = 'cartera_usuario'

class CategoriasGasto(models.Model):
    cg_id = models.CharField(max_length=10, primary_key=True, unique=True)
    nom_cg = models.CharField(max_length=50)

    @staticmethod
    def gen_id():
        n = 1
        while True:
            yield n
            n += 1
    
    g = gen_id()

    @classmethod
    def next_id(cls):
        return 'cg' + str(next(cls.g))
    
    @classmethod
    def create(cls, nom_cg):
        obj = cls(cg_id=cls.next_id(), nom_cg=nom_cg)
        obj.save()
        return obj 
    
    class Meta:
        db_table = 'categorias_gasto'

class SubcategoriasGasto(models.Model):
    scg_id = models.CharField(max_length=10, primary_key=True)
    nom_scg = models.CharField(max_length=50)
    cg_id = models.ForeignKey(CategoriasGasto, on_delete=models.PROTECT, db_column='cg_id')

    class Meta:
        db_table = 'subcategorias_gasto'


class CategoriasIngreso(models.Model):
    ci_id = models.CharField(max_length=10, primary_key=True)
    nom_ci = models.CharField(max_length=50)

    class Meta:
        db_table = 'categorias_ingreso'

class SubcategoriasIngreso(models.Model):
    sci_id = models.CharField(max_length=10, primary_key=True)
    nom_sci = models.CharField(max_length=50)
    ci_id = models.ForeignKey(CategoriasIngreso, on_delete=models.PROTECT, db_column='ci_id')

    class Meta:
        db_table = 'subcategorias_ingreso'

class TipoOperacion(models.Model):
    to_id = models.CharField(max_length=3, primary_key=True)
    nom_to = models.CharField(max_length=30)

    class Meta:
        db_table = 'tipo_operacion'

class OperacionesUsuario(models.Model):
    o_id = models.CharField(max_length=10, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.CASCADE, db_column='cu_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'operaciones_usuario'

class DetalleGasto(models.Model):
    dg_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField(OperacionesUsuario, on_delete=models.PROTECT, db_column='o_id')
    etiqueta = models.CharField(max_length=50)
    scg_id = models.ForeignKey(SubcategoriasGasto, on_delete=models.PROTECT, db_column='scg_id')

    class Meta:
        db_table = 'detalle_gasto'

class DetalleIngreso(models.Model):
    di_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField(OperacionesUsuario, on_delete=models.PROTECT, db_column='o_id')
    etiqueta = models.CharField(max_length=50)
    sci_id = models.ForeignKey(SubcategoriasIngreso, on_delete=models.PROTECT, db_column='sci_id')

    class Meta:
        db_table = 'detalle_ingreso'

class OperacionesUsuarioProgramadas(models.Model):


    op_id = models.CharField(max_length=10, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.PROTECT, db_column='cu_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(default=timezone.now)
    hora = models.TimeField
    activo = models.BooleanField(default=True)

    class Meta:
        db_table = 'operaciones_usuario_programadas'

    

class DetalleGastoProgramado(models.Model):
    dgp_id = models.CharField(max_length=10, primary_key=True)
    op_id = models.OneToOneField(OperacionesUsuarioProgramadas, on_delete=models.PROTECT, db_column='op_id')
    etiqueta = models.CharField(max_length=50)
    subsidiado = models.BooleanField(default=False)
    scg_id = models.ForeignKey(SubcategoriasGasto, on_delete=models.PROTECT, db_column='scg_id')

    class Meta:
        db_table = 'detalle_gasto_programado'

class DetalleIngresoProgramado(models.Model):
    dip_id = models.CharField(max_length=10, primary_key=True)
    op_id = models.OneToOneField(OperacionesUsuarioProgramadas, on_delete=models.PROTECT, db_column='op_id')
    etiqueta = models.CharField(max_length=50)
    sci_id = models.ForeignKey(SubcategoriasIngreso, on_delete=models.PROTECT, db_column='sci_id')

    class Meta:
        db_table = 'detalle_ingreso_programado'

class ProyeccionesFinancieras(models.Model):
    pf_id = models.CharField(max_length=20, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.PROTECT, db_column='op_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    etiqueta = models.CharField(max_length=50)
    fecha_inicio = models.DateField
    fecha_fin = models.DateField
    cantidad_proyeccion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad_progreso = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    class Meta:
        db_table = 'proyecciones_financieras'

class HistoricoProyeccionesFinancieras(models.Model):
    hpf_id = models.CharField(max_length=20, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.PROTECT, db_column='op_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    etiqueta = models.CharField(max_length=50)
    fecha_inicio = models.DateField
    fecha_fin = models.DateField
    cantidad_proyeccion = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    cantidad_final = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'historico_proyecciones_financieras'
