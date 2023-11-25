from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class SerializadorCarteraUsuario(serializers.ModelSerializer):
    class Meta:
        model = CarteraUsuario
        fields = ["saldo", "divisa"]

    def validate_saldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("Saldo invalido")
        
    def create(self, validated_data):
        user = CarteraUsuario.objects.create(
            u_id=Usuario.objects.get(pk=self.context.get('request').user.u_id),
            saldo=validated_data['saldo'],
            divisa=validated_data['divisa'])
        user.save()
        return user