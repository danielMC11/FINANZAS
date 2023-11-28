from rest_framework.authentication import SessionAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *


class CrearCartera(APIView):	
	def post(self, request, u_id):
		datos = request.data
		serializer = SerializadorCarteraUsuario(data=datos, context={'request': u_id}, many = False)
		if serializer.is_valid(raise_exception=True):
			cartera = serializer.create(datos)
			if cartera:
				return Response(serializer.data)
		return Response(status=status.HTTP_400_BAD_REQUEST)
