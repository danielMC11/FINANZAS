# Generated by Django 4.2.7 on 2023-11-25 18:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestor_cartera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasGasto',
            fields=[
                ('cg_id', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True)),
                ('nom_cg', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categorias_gasto',
            },
        ),
        migrations.CreateModel(
            name='CategoriasIngreso',
            fields=[
                ('ci_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_ci', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'categorias_ingreso',
            },
        ),
        migrations.CreateModel(
            name='TipoOperacion',
            fields=[
                ('to_id', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nom_to', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'tipo_operacion',
            },
        ),
        migrations.CreateModel(
            name='SubcategoriasIngreso',
            fields=[
                ('sci_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_sci', models.CharField(max_length=50)),
                ('ci_id', models.ForeignKey(db_column='ci_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.categoriasingreso')),
            ],
            options={
                'db_table': 'subcategorias_ingreso',
            },
        ),
        migrations.CreateModel(
            name='SubcategoriasGasto',
            fields=[
                ('scg_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_scg', models.CharField(max_length=50)),
                ('cg_id', models.ForeignKey(db_column='cg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.categoriasgasto')),
            ],
            options={
                'db_table': 'subcategorias_gasto',
            },
        ),
        migrations.CreateModel(
            name='OperacionesUsuario',
            fields=[
                ('o_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2023, 11, 25, 18, 26, 12, tzinfo=datetime.timezone.utc))),
                ('cu_id', models.ForeignKey(db_column='cu_id', on_delete=django.db.models.deletion.CASCADE, to='gestor_cartera.carterausuario')),
                ('to_id', models.ForeignKey(db_column='to_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.tipooperacion')),
            ],
            options={
                'db_table': 'operaciones_usuario',
            },
        ),
        migrations.CreateModel(
            name='DetalleIngreso',
            fields=[
                ('di_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('etiqueta', models.CharField(max_length=50)),
                ('o_id', models.OneToOneField(db_column='o_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.operacionesusuario')),
                ('sci_id', models.ForeignKey(db_column='sci_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.subcategoriasingreso')),
            ],
            options={
                'db_table': 'detalle_ingreso',
            },
        ),
        migrations.CreateModel(
            name='DetalleGasto',
            fields=[
                ('dg_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('etiqueta', models.CharField(max_length=50)),
                ('o_id', models.OneToOneField(db_column='o_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.operacionesusuario')),
                ('scg_id', models.ForeignKey(db_column='scg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.subcategoriasgasto')),
            ],
            options={
                'db_table': 'detalle_gasto',
            },
        ),
    ]