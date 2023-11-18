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
		data = request.data
		usr = request.user.u_id
		usuario = Usuario.objects.get(pk=usr)
		cartera = CarteraUsuario.objects.create(
			cu_id = data['cu_id'],
			u_id = usuario,
			saldo = data['saldo'],
			divisa = data['divisa']
        )
		serializer = SerializadorCarteraUsuario(cartera, many = False)
		return Response(serializer.data)
	







		