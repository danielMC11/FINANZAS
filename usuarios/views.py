from django.contrib.auth import get_user_model, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SerializadorRegistroUsuario, SeralizadorLoginUsuario, SerializadorUsuario
from rest_framework import permissions, status
from gestor_cartera.models import CarteraUsuario
from usuarios.models import Usuario
from django.core.exceptions import ObjectDoesNotExist

class RegistroUsuario(APIView):
	def post(self, request):
		datos = request.data
		serializer = SerializadorRegistroUsuario(data=datos)
		if serializer.is_valid(raise_exception=True):
			usuario = serializer.crear(datos)
			if usuario:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginUsuario(APIView):
	def post(self, request):
		datos = request.data
		serializer = SeralizadorLoginUsuario(data=datos)
		if serializer.is_valid(raise_exception=True):
			usuario = serializer.comprobar_usuario(datos)
			if not usuario:
				return Response(status=status.HTTP_400_BAD_REQUEST)
			try:	
				CarteraUsuario.objects.get(u_id=usuario.u_id)
			except ObjectDoesNotExist:
				return Response({'u_id': usuario.u_id,'cartera': False}, status=status.HTTP_200_OK)
			else:
				return Response({'u_id': usuario.u_id, 'cartera': True}, status=status.HTTP_200_OK)


class LogoutUsuario(APIView):
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class PerfilUsuario(APIView):
	def get(self, request, u_id):
		serializer = SerializadorUsuario(Usuario.objects.get(pk=u_id))
		return Response({'Usuario': serializer.data}, status=status.HTTP_200_OK)

