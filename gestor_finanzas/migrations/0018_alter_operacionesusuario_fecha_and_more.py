# Generated by Django 4.2.7 on 2023-11-25 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_finanzas', '0017_alter_operacionesusuario_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacionesusuario',
            name='fecha',
            field=models.DateTimeField(default=datetime.time(11, 48, 37)),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='hora',
            field=models.TimeField(default=datetime.datetime(2023, 11, 25, 16, 48, 37, tzinfo=datetime.timezone.utc)),
        ),
    ]
