from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class AdminUsuarios(BaseUserManager):
	def crear_usuario(self, email, password=None):
		email = self.normalize_email(email)
		user = self.model(email=email)
		user.set_password(password)
		user.save()
		return user



class Usuario(AbstractBaseUser, PermissionsMixin):
	u_id = models.CharField(max_length=10, primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	USERNAME_FIELD = 'email'

	objects = AdminUsuarios()

	def save(self, *args, **kwargs):
		if not self.u_id:
			self.u_id = f"u{Usuario.objects.count() + 1}"
		return super().save(*args, **kwargs)
	
	class Meta:
		db_table = 'usuarios'
