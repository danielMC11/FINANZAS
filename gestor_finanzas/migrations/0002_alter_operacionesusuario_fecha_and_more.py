# Generated by Django 4.2.7 on 2023-11-06 20:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_finanzas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacionesusuario',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='fecha',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]