from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class RegistrarOperacionProgramadaIngreso(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def post(self, request):
		datos = request.data
		serializer = SerializadorOperacionesProgramadasUsuarioIngreso(data=datos, context={'request': request}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion_programada = serializer.create(datos)
		if operacion_programada:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	

class RegistrarOperacionProgramadaGasto(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def post(self, request):
		datos = request.data
		serializer = SerializadorOperacionesProgramadasUsuarioGasto(data=datos, context={'request': request}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion_programada = serializer.create(datos)
		if operacion_programada:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)