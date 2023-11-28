from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *



class VisualizarCategoriasIngreso(APIView):
	def get(self, request):
		categorias = CategoriasIngreso.objects.all()
		serializer = SerializadorCategoriasIngreso(categorias, many=True)
		return Response(serializer.data)
	

class VisualizarSubcategoriasIngreso(APIView):
	def get(self, request):
		categorias = SubcategoriasIngreso.objects.all()
		serializer = SerializadorSubcategoriasIngreso(categorias, many=True)
		return Response(serializer.data)


class VisualizarCategoriasGasto(APIView):
	def get(self, request):
		categorias = CategoriasGasto.objects.all()
		serializer = SerializadorCategoriasGasto(categorias, many=True)
		return Response(serializer.data)
	

class VisualizarSubcategoriasGasto(APIView):
	def get(self, request):
		categorias = SubcategoriasGasto.objects.all()
		serializer = SerializadorSubcategoriasGasto(categorias, many=True)
		return Response(serializer.data)
	

class RegistrarOperacionIngreso(APIView):
	def post(self, request, u_id):
		datos = request.data
		serializer = SerializadorOperacionesUsuarioIngreso(data=datos, context={'request': u_id}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion = serializer.create(datos)
		if operacion:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)


class RegistrarOperacionGasto(APIView):
	def post(self, request, u_id):
		datos = request.data
		serializer = SerializadorOperacionesUsuarioGasto(data=datos, context={'request': u_id}, many = False)

		if serializer.is_valid(raise_exception=True):
			operacion = serializer.create(datos)
		if operacion:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)

class VisualizarExtractos(APIView):
	def get(self, request, u_id):
		extractos = OperacionesUsuario.extractos_operaciones(u_id)
		serializer = SerializadorExtractos(extractos, many=True)
		return Response(serializer.data)

class VisualizarExtractoDetalleIngreso(APIView):
	def get(self, request, o_id, u_id):
		detalle_extracto_ingreso = OperacionesUsuario.extracto_detalle(u_id, o_id)
		serializer = SerializadorExtractoDetalleIngreso(detalle_extracto_ingreso, many=False)
		return Response(serializer.data)
	
class VisualizarExtractoDetalleGasto(APIView):
	def get(self, request, o_id, u_id):
		detalle_extracto_gasto = OperacionesUsuario.extracto_detalle(u_id, o_id)
		serializer = SerializadorExtractoDetalleGasto(detalle_extracto_gasto, many=False)
		return Response(serializer.data)
