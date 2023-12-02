from django.shortcuts import render

# Create your views here.



from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class CrearProyeccion(APIView):
	def post(self, request, u_id):
		datos = request.data
		serializer = SerializadorProyecciones(data=datos, context={'request': u_id}, many = False)
		if serializer.is_valid(raise_exception=True):
			proyeccion = serializer.create(datos)
			if proyeccion:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	