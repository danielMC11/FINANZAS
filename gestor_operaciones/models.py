from django.db import models
from gestor_cartera.models import CarteraUsuario
from django.utils import timezone

class CategoriasGasto(models.Model):
    cg_id = models.CharField(max_length=10, primary_key=True, unique=True)
    nom_cg = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'categorias_gasto'

class SubcategoriasGasto(models.Model):
    scg_id = models.CharField(max_length=10, primary_key=True)
    nom_scg = models.CharField(max_length=50)
    cg_id = models.ForeignKey(CategoriasGasto, on_delete=models.PROTECT, db_column='cg_id')

    def __str__(self):
        return f'{self.nom_scg} ({self.cg_id.nom_cg})'

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

    def __str__(self):
        return f'{self.nom_sci} ({self.ci_id.nom_ci})'
    
    class Meta:
        db_table = 'subcategorias_ingreso'

class TipoOperacion(models.Model):
    to_id = models.CharField(max_length=3, primary_key=True)
    nom_to = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.nom_to}'

    class Meta:
        db_table = 'tipo_operacion'

class OperacionesUsuario(models.Model):
    o_id = models.CharField(max_length=10, primary_key=True)
    cu_id = models.ForeignKey(CarteraUsuario, on_delete=models.CASCADE, db_column='cu_id')
    to_id = models.ForeignKey(TipoOperacion, on_delete=models.PROTECT, db_column='to_id')
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha = models.DateTimeField(default=timezone.localtime(timezone.now(), timezone.get_fixed_timezone(-300) ).replace(microsecond=0))

    def save(self, *args, **kwargs):
        if not self.o_id:
            self.o_id = f"o{OperacionesUsuario.objects.count() + 1}"
        return super().save(*args, **kwargs)
    @classmethod
    def extractos_operaciones(cls, u_id):
        cartera=CarteraUsuario.objects.get(u_id=u_id)
        extractos = cls.objects.raw(''' 
		select o_id, cantidad, nom_to as tipo_operacion, cantidad, divisa, fecha from operaciones_usuario
        join cartera_usuario using(cu_id) join usuarios using(u_id) join
        tipo_operacion using(to_id) where cu_id=%s and 
        (o_id in (select o_id from detalle_ingreso) or o_id in (select o_id from detalle_gasto))
		''', [cartera.cu_id])

        return extractos
    #  cantidad, nom_to, etiqueta, nom_sci, nom._0
    # .ci, divisa, fecha 

    @classmethod
    def extracto_detalle_ingreso(cls, u_id, o_id):
        cartera=CarteraUsuario.objects.get(u_id=u_id)
        detalle_extracto = cls.objects.raw('''
        select o_id, cantidad, nom_to as tipo_operacion, etiqueta, nom_sci as subcategoria_ingreso, nom_ci as categoria_ingreso, divisa, fecha  from
        operaciones_usuario join cartera_usuario using(cu_id) join tipo_operacion using(to_id)
        join detalle_ingreso using(o_id) join subcategorias_ingreso using(sci_id) join categorias_ingreso
        using(ci_id) where cu_id=%s and o_id=%s LIMIT 1
		''', [cartera.cu_id, o_id])

        return list(detalle_extracto)[0]
    
    @classmethod
    def extracto_detalle_gasto(cls, u_id, o_id):
        cartera=CarteraUsuario.objects.get(u_id=u_id)
        detalle_extracto = cls.objects.raw('''
        select o_id, cantidad, nom_to as tipo_operacion, etiqueta, nom_scg as subcategoria_gasto, nom_cg as categoria_gasto, divisa, fecha  from
        operaciones_usuario join cartera_usuario using(cu_id) join tipo_operacion using(to_id)
        join detalle_gasto using(o_id) join subcategorias_gasto using(scg_id) join categorias_gasto
        using(cg_id) where  cu_id = %s and o_id=%s LIMIT 1
		''', [cartera.cu_id, o_id])

        return list(detalle_extracto)[0]
    
    class Meta:
        db_table = 'operaciones_usuario'

class DetalleGasto(models.Model):
    dg_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField(OperacionesUsuario, on_delete=models.PROTECT, db_column='o_id')
    etiqueta = models.CharField(max_length=50)
    scg_id = models.ForeignKey(SubcategoriasGasto, on_delete=models.PROTECT, db_column='scg_id')

    def save(self, *args, **kwargs):
        if not self.dg_id:
            self.dg_id = f"dg{DetalleGasto.objects.count() + 1}"
        return super().save(*args, **kwargs)

    class Meta:
        db_table = 'detalle_gasto'

class DetalleIngreso(models.Model):
    di_id = models.CharField(max_length=10, primary_key=True)
    o_id = models.OneToOneField(OperacionesUsuario, on_delete=models.PROTECT, db_column='o_id')
    etiqueta = models.CharField(max_length=50)
    sci_id = models.ForeignKey(SubcategoriasIngreso, on_delete=models.PROTECT, db_column='sci_id')

    def save(self, *args, **kwargs):
        if not self.di_id:
            self.di_id = f"di{DetalleIngreso.objects.count() + 1}"
        return super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'detalle_ingreso'
