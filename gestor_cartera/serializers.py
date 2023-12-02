from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import *

class SerializadorCarteraUsuario(serializers.ModelSerializer):
    class Meta:
        model = CarteraUsuario
        fields = ["saldo", "div_id"]

    def validate_saldo(self, value):
        if value <= 0:
            raise serializers.ValidationError("Saldo invalido")
        
    def create(self, validated_data):
        divisa = Divisas.objects.get(pk=validated_data['div_id'])
        user = CarteraUsuario.objects.create(
            u_id=Usuario.objects.get(pk=self.context.get('request')),
            saldo=validated_data['saldo'],
            div_id=divisa)
        user.save()
        return user