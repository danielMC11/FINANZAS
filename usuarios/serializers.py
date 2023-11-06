from django.core.exceptions import ValidationError
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

UserModel = get_user_model()

class SerializadorRegistroUsuario(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = '__all__'
	def crear(self, datos):
		obj_usuario = UserModel.objects.crear_usuario(email=datos['email'], password=datos['password'])
		obj_usuario.nombres = datos['nombres']
		obj_usuario.apellidos = datos['apellidos']
		obj_usuario.save()
		return obj_usuario

class SeralizadorLoginUsuario(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	
	def comprobar_usuario(self, datos):
		usuario = authenticate(username=datos['email'], password=datos['password'])
		if not usuario:
			raise ValidationError('Usuario no encontrado')
		return usuario

class SerializadorUsuario(serializers.ModelSerializer):
	class Meta:
		model = UserModel
		fields = ('u_id', 'email', 'nombres', 'apellidos')



