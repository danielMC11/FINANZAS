from django.contrib.auth import get_user_model, login, logout
from rest_framework.authentication import SessionAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SerializadorRegistroUsuario, SeralizadorLoginUsuario, SerializadorUsuario
from rest_framework import permissions, status
from gestor_cartera.models import CarteraUsuario
from django.core.exceptions import ObjectDoesNotExist

class RegistroUsuario(APIView):
	permission_classes = (permissions.AllowAny,)
	def post(self, request):
		datos = request.data
		serializer = SerializadorRegistroUsuario(data=datos)
		if serializer.is_valid(raise_exception=True):
			usuario = serializer.crear(datos)
			if usuario:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class LoginUsuario(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = (SessionAuthentication,)
	##
	def post(self, request):
		datos = request.data
		serializer = SeralizadorLoginUsuario(data=datos)
		if serializer.is_valid(raise_exception=True):
			usuario = serializer.comprobar_usuario(datos)
			login(request, usuario)
			try:
				CarteraUsuario.objects.get(u_id=request.user.u_id)
			except ObjectDoesNotExist:
				return Response({'cartera': False}, status=status.HTTP_200_OK)
			else:
				return Response({'cartera': True}, status=status.HTTP_200_OK)


class LogoutUsuario(APIView):
	permission_classes = (permissions.AllowAny,)
	authentication_classes = ()
	def post(self, request):
		logout(request)
		return Response(status=status.HTTP_200_OK)


class Usuario(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	##
	def get(self, request):
		serializer = SerializadorUsuario(request.user)
		return Response({'Usuario': serializer.data}, status=status.HTTP_200_OK)

