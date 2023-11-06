from rest_framework import serializers
from .models import *

class SerializadorCarteraUsuario(serializers.ModelSerializer):
    class Meta:
        model = CarteraUsuario
        fields = '__all__'