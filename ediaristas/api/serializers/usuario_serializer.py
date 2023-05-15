from rest_framework import serializers
from ..models import Usuario;

class UsuarioSerializer(serializers.ModelSerializer):
  chave_pix = serializers.CharField(required=False)
  password_confirmation = serializers.CharField(write_only=True, required=True)#apenas para confirmar a escrita
  tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)
  foto_usuario = serializers.ImageField(max_length=None, required=False, use_url=True, allow_null=True)
  password = serializers.CharField(write_only=True)
  foto_documento = serializers.ImageField(write_only=True, required=True)
  
  class Meta:
    model = Usuario
    fields = (
      'nome_completo',
      'cpf',
      'nascimento',
      'foto_documento',
      'telefone',
      'tipo_usuario',
      'password',
      'password_confirmation',
      'email',
      'chave_pix',
      'foto_usuario'
    )
    
    
#Aqui estamos serializando os campos, porém existe campos que não são obrigatórios, pois temos dois tipos de usuários, os clientes e os diáriatas, que no caso um tem campo obrigatório que o outro não tem