# Generated by Django 4.2.7 on 2023-11-26 19:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_operaciones', '0005_alter_operacionesusuario_fecha_operacion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacionesusuario',
            name='fecha_operacion',
            field=models.DateField(default=datetime.datetime(2023, 11, 26, 19, 14, 18, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='operacionesusuario',
            name='hora_operacion',
            field=models.TimeField(default=datetime.time(14, 14, 18)),
        ),
        migrations.AlterModelTable(
            name='operacionesusuario',
            table=None,
        ),
    ]
