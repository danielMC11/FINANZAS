# Generated by Django 4.2.7 on 2023-11-25 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_finanzas', '0021_diasemana_alter_operacionesusuario_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacionesusuario',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 25, 17, 14, 6, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='fecha',
            field=models.DateTimeField(default=datetime.time(12, 14, 6)),
        ),
        migrations.AlterModelTable(
            name='diasemana',
            table='dia_semana',
        ),
    ]
