from rest_framework import serializers
from ..models import Usuario

class DiaristasLocalidadesSerializer(serializers.ModelSerializer):
  cidade = serializers.SerializerMethodField()
  class Meta:
    model = Usuario
    fields = ('nome_completo', 'reputacao', 'foto_usuario', 'cidade')
    #quando o objeto entrar no serializer vai retornar esses campos
  
  def get_cidade(self, obj):
    return "Paraná"