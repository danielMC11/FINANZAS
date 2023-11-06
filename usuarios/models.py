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
	u_id = models.AutoField(primary_key=True)
	email = models.EmailField(max_length=50, unique=True)
	nombres = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nombres', 'apellidos']

	objects = AdminUsuarios()

	def __str__(self):
		return f'{self.nombres} {self.apellidos}'
