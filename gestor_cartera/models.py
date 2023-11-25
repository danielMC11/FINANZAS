from django.db import models
from usuarios.models import Usuario
from django.utils import timezone



class CarteraUsuario(models.Model):
    cu_id = models.CharField(max_length=10, primary_key=True)
    u_id = models.OneToOneField(Usuario, on_delete=models.CASCADE, db_column='u_id')
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    divisa = models.CharField(max_length=3)

    def save(self, *args, **kwargs):
        if not self.cu_id:
            self.cu_id = f"cu{CarteraUsuario.objects.count() + 1}"
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.u_id.nombres} / {self.u_id.email} / {self.cu_id}'

    class Meta:
        db_table = 'cartera_usuario'