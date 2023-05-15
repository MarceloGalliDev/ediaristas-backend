from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
  chave_pix = serializers.CharField(required=False)
  password_confirmation = serializers.CharField(write_only=True, required=True)#apenas para confirmar a escrita
  tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)
  foto_usuario = serializers.ImageField(max_length=None, required=False, use_url=True, allow_null=True)
  password = serializers.CharField(write_only=True)
  foto_documento = serializers.ImageField(write_only=True, required=True)
  
  class Meta:
    model = Usuario
    #Aqui estamos serializando os campos, porém existe campos que não são obrigatórios, 
    #pois temos dois tipos de usuários, os clientes e os diáriatas, que no caso um tem 
    #campo obrigatório que o outro não tem
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
    
  #validação do password com confirmation_password
  def validate_password(self, password):
    password_confirmation = self.initial_data['password_confirmation']
    if password != password_confirmation:
      raise serializers.ValidationError('Senhas não combinam!')
    return password
    
  #estamos subscrevendo o método create()  
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data.get('password'))
    #aqui estamos passando o pop para não salvar no banco de dados essa informação
    validated_data.pop('password_confirmation', None)
    usuario = Usuario.objects.create(**validated_data)
    return usuario