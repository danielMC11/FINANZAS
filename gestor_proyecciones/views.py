from django.shortcuts import render

# Create your views here.

from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *

class CrearProyeccion(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	authentication_classes = (SessionAuthentication,)
	def post(self, request):
		datos = request.data
		serializer = SerializadorProyecciones(data=datos, context={'request': request.user.u_id}, many = False)
		if serializer.is_valid(raise_exception=True):
			proyeccion = serializer.create(datos)
			if proyeccion:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
	