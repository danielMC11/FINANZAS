from django.db import models
from usuarios.models import Usuario
from django.utils import timezone


class Divisas(models.Model):
    div_id = models.CharField(max_length=10, primary_key=True)
    nom_div = models.CharField(max_length=3)
    pais = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f'{self.nom_div}'
    
    class Meta:
        db_table = 'divisas'


class CarteraUsuario(models.Model):
    cu_id = models.CharField(max_length=10, primary_key=True)
    u_id = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='u_id')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    div_id = models.ForeignKey(Divisas, on_delete=models.PROTECT, db_column='div_id')

    def save(self, *args, **kwargs):
        if not self.cu_id:
            self.cu_id = f"cu{CarteraUsuario.objects.count() + 1}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.u_id.nombres} / {self.u_id.email} / {self.cu_id}'

    class Meta:
        db_table = 'cartera_usuario'


