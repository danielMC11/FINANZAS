# Generated by Django 4.2.7 on 2023-11-27 03:30

from django.db import migrations, models
import gestor_operaciones.utils


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_operaciones_programadas', '0006_remove_operacionesusuarioprogramadas_hora_programada_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='fecha_operacion',
            field=models.DateField(default=gestor_operaciones.utils.fecha_actual),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='hora_operacion',
            field=models.TimeField(default=gestor_operaciones.utils.hora_actual),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='hora_programada_desde',
            field=models.TimeField(default=gestor_operaciones.utils.hora_actual),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='hora_programada_hasta',
            field=models.TimeField(default=gestor_operaciones.utils.adicion_hora_actual),
        ),
    ]
