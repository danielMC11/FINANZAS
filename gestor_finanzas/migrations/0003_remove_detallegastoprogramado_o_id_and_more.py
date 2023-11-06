# Generated by Django 4.2.7 on 2023-11-06 21:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestor_finanzas', '0002_alter_operacionesusuario_fecha_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detallegastoprogramado',
            name='o_id',
        ),
        migrations.AddField(
            model_name='detallegastoprogramado',
            name='op_id',
            field=models.OneToOneField(db_column='op_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.operacionesusuarioprogramadas'),
        ),
        migrations.AlterField(
            model_name='carterausuario',
            name='u_id',
            field=models.OneToOneField(db_column='u_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='detallegasto',
            name='o_id',
            field=models.OneToOneField(db_column='o_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.operacionesusuario'),
        ),
        migrations.AlterField(
            model_name='detallegasto',
            name='scg_id',
            field=models.ForeignKey(db_column='scg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.subcategoriasgasto'),
        ),
        migrations.AlterField(
            model_name='detallegastoprogramado',
            name='scg_id',
            field=models.ForeignKey(db_column='scg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.subcategoriasgasto'),
        ),
        migrations.AlterField(
            model_name='detalleingreso',
            name='o_id',
            field=models.OneToOneField(db_column='o_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.operacionesusuario'),
        ),
        migrations.AlterField(
            model_name='detalleingreso',
            name='sci_id',
            field=models.ForeignKey(db_column='sci_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.subcategoriasingreso'),
        ),
        migrations.AlterField(
            model_name='detalleingresoprogramado',
            name='op_id',
            field=models.OneToOneField(db_column='op_id', null=True, on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.operacionesusuarioprogramadas'),
        ),
        migrations.AlterField(
            model_name='detalleingresoprogramado',
            name='sci_id',
            field=models.ForeignKey(db_column='sci_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.subcategoriasingreso'),
        ),
        migrations.AlterField(
            model_name='historicoplanesgasto',
            name='cg_id',
            field=models.ForeignKey(db_column='cg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.categoriasgasto'),
        ),
        migrations.AlterField(
            model_name='historicoplanesgasto',
            name='cu_id',
            field=models.ForeignKey(db_column='cu_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.carterausuario'),
        ),
        migrations.AlterField(
            model_name='operacionesusuario',
            name='cu_id',
            field=models.ForeignKey(db_column='cu_id', on_delete=django.db.models.deletion.CASCADE, to='gestor_finanzas.carterausuario'),
        ),
        migrations.AlterField(
            model_name='operacionesusuario',
            name='to_id',
            field=models.ForeignKey(db_column='to_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.tipooperacion'),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='cu_id',
            field=models.ForeignKey(db_column='cu_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.carterausuario'),
        ),
        migrations.AlterField(
            model_name='operacionesusuarioprogramadas',
            name='to_id',
            field=models.ForeignKey(db_column='to_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.tipooperacion'),
        ),
        migrations.AlterField(
            model_name='planesgasto',
            name='cg_id',
            field=models.ForeignKey(db_column='cg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.categoriasgasto'),
        ),
        migrations.AlterField(
            model_name='planesgasto',
            name='cu_id',
            field=models.ForeignKey(db_column='op_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.carterausuario'),
        ),
        migrations.AlterField(
            model_name='subcategoriasgasto',
            name='cg_id',
            field=models.ForeignKey(db_column='cg_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.categoriasgasto'),
        ),
        migrations.AlterField(
            model_name='subcategoriasingreso',
            name='ci_id',
            field=models.ForeignKey(db_column='ci_id', on_delete=django.db.models.deletion.PROTECT, to='gestor_finanzas.categoriasingreso'),
        ),
    ]
