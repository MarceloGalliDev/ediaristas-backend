from rest_framework import serializers
from ..models import Usuario

class DiaristasLocalidadesSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ('nome_completo', 'reputacao', 'foto_usuario')#quando o objeto entrar no serializer vai retornar esses campos