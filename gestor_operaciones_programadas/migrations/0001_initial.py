# Generated by Django 4.2.7 on 2023-11-28 20:55

from django.db import migrations, models
import django.db.models.deletion
import gestor_operaciones.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gestor_operaciones', '0001_initial'),
        ('gestor_cartera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaSemana',
            fields=[
                ('d_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_dia', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'dia_semana',
            },
        ),
        migrations.CreateModel(
            name='OperacionesUsuarioProgramadas',
            fields=[
                ('op_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('cantidad', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('etiqueta', models.CharField(default='', max_length=50)),
                ('fecha_operacion', models.DateField(default=gestor_operaciones.utils.fecha_actual)),
                ('hora_operacion', models.TimeField(default=gestor_operaciones.utils.hora_actual)),
                ('hora_programada_desde', models.TimeField(default=gestor_operaciones.utils.hora_actual)),
                ('hora_programada_hasta', models.TimeField(default='00:00:00')),
                ('activo', models.BooleanField(default=True)),
                ('cu_id', models.ForeignKey(db_column='cu_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_cartera.carterausuario')),
                ('dias', models.ManyToManyField(to='gestor_operaciones_programadas.diasemana')),
                ('to_id', models.ForeignKey(db_column='to_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.tipooperacion')),
            ],
            options={
                'db_table': 'operaciones_usuario_programadas',
            },
        ),
        migrations.CreateModel(
            name='DetalleIngresoProgramado',
            fields=[
                ('dip_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('op_id', models.OneToOneField(db_column='op_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones_programadas.operacionesusuarioprogramadas')),
                ('sci_id', models.ForeignKey(db_column='sci_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.subcategoriasingreso')),
            ],
            options={
                'db_table': 'detalle_ingreso_programado',
            },
        ),
        migrations.CreateModel(
            name='DetalleGastoProgramado',
            fields=[
                ('dgp_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('op_id', models.OneToOneField(db_column='op_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones_programadas.operacionesusuarioprogramadas')),
                ('scg_id', models.ForeignKey(db_column='scg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_operaciones.subcategoriasgasto')),
            ],
            options={
                'db_table': 'detalle_gasto_programado',
            },
        ),
    ]
