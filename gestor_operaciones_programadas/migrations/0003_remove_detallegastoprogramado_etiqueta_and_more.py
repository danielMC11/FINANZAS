# Generated by Django 4.2.7 on 2023-11-26 00:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_operaciones_programadas', '0002_remove_detallegastoprogramado_subsidiado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallegastoprogramado',
            name='etiqueta',
        ),
        migrations.RemoveField(
            model_name='detalleingresoprogramado',
            name='etiqueta',
        ),
        migrations.AddField(
            model_name='operacionesusuarioprogramadas',
            name='etiqueta',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 26, 0, 6, 57, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='hora',
            field=models.TimeField(default=datetime.time(19, 6, 57)),
        ),
    ]