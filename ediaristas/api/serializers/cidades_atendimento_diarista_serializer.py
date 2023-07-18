from rest_framework import serializers
from ..models import CidadesAtendidas

class CidadesAtendidasDiaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CidadesAtendidas
        fields = '__all__'