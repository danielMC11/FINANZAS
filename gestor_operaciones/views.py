from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


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

class VisualizarExtractos(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def get(self, request):
		extractos = OperacionesUsuario.extractos_operaciones(request.user.u_id)
		serializer = SerializadorExtractos(extractos, many=True)
		return Response(serializer.data)

class VisualizarExtractoDetalleIngreso(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def get(self, request, o_id):
		detalle_extracto_ingreso = OperacionesUsuario.extracto_detalle(request.user.u_id, o_id)
		serializer = SerializadorExtractoDetalleIngreso(detalle_extracto_ingreso, many=False)
		return Response(serializer.data)
	
class VisualizarExtractoDetalleGasto(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)

	def get(self, request, o_id):
		detalle_extracto_gasto = OperacionesUsuario.extracto_detalle(request.user.u_id, o_id)
		serializer = SerializadorExtractoDetalleGasto(detalle_extracto_gasto, many=False)
		return Response(serializer.data)
