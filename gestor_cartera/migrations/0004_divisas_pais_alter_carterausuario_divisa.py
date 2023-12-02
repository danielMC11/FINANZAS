# Generated by Django 4.2.7 on 2023-12-02 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_cartera', '0003_divisas'),
    ]

    operations = [
        migrations.AddField(
            model_name='divisas',
            name='pais',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='carterausuario',
            name='divisa',
            field=models.ForeignKey(db_column='div_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_cartera.divisas'),
        ),
    ]