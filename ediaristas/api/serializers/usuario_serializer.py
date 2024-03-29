from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from ..models import Usuario
from datetime import date
from rest_framework_simplejwt.tokens import RefreshToken
from ..services import usuario_service
from ..hateoas import Hateoas
from django.urls import reverse

class UsuarioSerializer(serializers.ModelSerializer):
  chave_pix = serializers.CharField(required=False)
  password_confirmation = serializers.CharField(write_only=True, required=True)#apenas para confirmar a escrita
  tipo_usuario = serializers.ChoiceField(choices=Usuario.TIPO_USUARIO_CHOICES)
  foto_usuario = serializers.ImageField(max_length=None, required=False, use_url=True, allow_null=True)
  password = serializers.CharField(write_only=True)
  foto_documento = serializers.ImageField(write_only=True, required=True)
  token = serializers.SerializerMethodField(required=False)
  links = serializers.SerializerMethodField(required=False)
  
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
      'foto_usuario',
      'token',
      'links',
    )
  
  #é retornado para o serializer devido ao SerializerMethodField
  def get_token(self, user):
    tokens = RefreshToken.for_user(user)
    data = {
      "refresh": str(tokens),
      "access": str(tokens.access_token)
    }
    return data
    
  def get_links(self, user):
    usuario = usuario_service.listar_usuario_email(user.email)
    links = Hateoas()
    links.add_get('lista_diarias', reverse=('diaria_lista'))
    if usuario.tipo_usuario == 1:
      links.add_post('cadastrar_diaria', reverse('diarias-list'))
    else:
      links.add_put('cadastrar_endereco', reverse('endereco-diarista-detail'))
      links.add_put('relacionar_cidades', reverse('cidades-atendimento-diarista-detail'))
    return links.to_array()
    
  def validate_password(self, password):
    password_confirmation = self.initial_data['password_confirmation']
    if password != password_confirmation:
      raise serializers.ValidationError('Senhas não combinam!')
    return password
    
  def validate_nascimento(self, nascimento):
    data_atual = date.today()
    idade = data_atual.year - nascimento.year - (
      (data_atual.month, data_atual.day) < (nascimento.month, nascimento.day)
    )
    if idade < 18:
      raise serializers.ValidationError("Usuário menor de idade.")
    if idade > 100:
      raise serializers.ValidationError("Idade maior que a permitida.")
    return nascimento
    
  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data.get('password'))
    validated_data.pop('password_confirmation', None)
    reputacao_geral = 2
    if validated_data['tipo_usuario'] == 2:
      reputacao_geral = Usuario.diarista_objects.reputacao_geral()['reputacao__avg']
      if reputacao_geral is None:
        reputacao_geral = 5
    usuario = Usuario.objects.create(reputacao = reputacao_geral, **validated_data)
    return usuario
  

#Aqui estamos serializando os campos, porém existe campos que não são obrigatórios, 
#pois temos dois tipos de usuários, os clientes e os diáriatas, que no caso um tem 
#campo obrigatório que o outro não tem

#validação do password com confirmation_password
  
#estamos subscrevendo o método create()  

#aqui estamos passando o pop para não salvar no banco de dados essa informação