# Generated by Django 4.2.7 on 2023-12-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor_cartera', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Divisas',
            fields=[
                ('div_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('nom_div', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'divisas',
            },
        ),
    ]
