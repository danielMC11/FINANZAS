from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from gestor_operaciones.serializers import SerializadorOperacionesUsuarioIngreso, SerializadorOperacionesUsuarioGasto
from .serializers import *
from .models import *


class RegistrarOperacionProgramadaIngreso(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	def post(self, request):
		datos = request.data
		serializer = SerializadorOperacionesProgramadasUsuarioIngreso(data=datos, context={'request': request.user.u_id}, many = False)

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
		serializer = SerializadorOperacionesProgramadasUsuarioGasto(data=datos, context={'request': request.user.u_id}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion_programada = serializer.create(datos)
		if operacion_programada:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	

class VisualizarOperacionesHabilitadas(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	def get(self, request):
		habilitadas = OperacionesUsuarioProgramadas.operaciones_habilitadas(request.user.u_id)
		serializer = SerializadorOperacionesHabilitadas(habilitadas, many=True)
		return Response(serializer.data)
	

class VisualizarOperacionesProgramadas(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	def get(self, request):
		all_operaciones_programdas = OperacionesUsuarioProgramadas.operaciones_programadas(request.user.u_id)
		serializer = SerializadorListadoOperacionesProgramadas(all_operaciones_programdas, many=True)
		return Response(serializer.data)
	

class ConfirmarOperacionProgramada(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	def post(self, request, op_id):
		datos = OperacionesUsuarioProgramadas.operacion_info(op_id)

		serializer = None
		if datos['to_id'] == 'to1':
			serializer = SerializadorOperacionesUsuarioIngreso(data=datos, context={'request': request.user.u_id}, many = False)
		elif datos['to_id'] == 'to2':
			serializer = SerializadorOperacionesUsuarioGasto(data=datos, context={'request': request.user.u_id}, many = False)
		else:
			Response(status=status.HTTP_400_BAD_REQUEST)
			
		if serializer.is_valid(raise_exception=True):
			operacion_programada = serializer.create(datos)
		if operacion_programada:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)