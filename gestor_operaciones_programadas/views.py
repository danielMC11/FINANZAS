from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class RegistrarOperacionProgramadaIngreso(APIView):
	def post(self, request, u_id):
		datos = request.data
		serializer = SerializadorOperacionesProgramadasUsuarioIngreso(data=datos, context={'request': u_id}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion_programada = serializer.create(datos)
		if operacion_programada:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	

class RegistrarOperacionProgramadaGasto(APIView):
	def post(self, request, u_id):
		datos = request.data
		serializer = SerializadorOperacionesProgramadasUsuarioGasto(data=datos, context={'request': u_id}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion_programada = serializer.create(datos)
		if operacion_programada:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	

class VisualizarOperacionesHabilitadas(APIView):
	def get(self, request, u_id):
		habilitadas = OperacionesUsuarioProgramadas.operaciones_habilitadas(u_id)
		serializer = SerializadorOperacionesHabilitadas(habilitadas, many=True)
		return Response(serializer.data)