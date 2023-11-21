from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class CrearCartera(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	
	def post(self, request):
		datos = request.data
		serializer = SerializadorCarteraUsuario(data=datos, context={'request': request}, many = False)
		
		if serializer.is_valid(raise_exception=True):
			cartera = serializer.create(datos)
			if cartera:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class RegistrarOperacionIngreso(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def post(self, request):
		datos = request.data
		serializer = SerializadorOperacionesUsuarioIngreso(data=datos, context={'request': request}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion = serializer.create(datos)
		if operacion:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrarOperacionGasto(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def post(self, request):
		datos = request.data
		serializer = SerializadorOperacionesUsuarioGasto(data=datos, context={'request': request}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion = serializer.create(datos)
		if operacion:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)





		