import requests
import json
from rest_framework import serializers
from .usuario_service import listar_usuario_id
from ..models import CidadesAtendidas


def cadastrar_cidade(codigo_ibge, cidade, estado):
  #esse método busca na tabela CidadeAtendimento se existe alguma cidade com código do ibge que estamos buscando, se existir retorne se não existir crie-o
  return CidadesAtendidas.objects.get_or_create(codigo_ibge=codigo_ibge, defaults=dict(
    #campos que queremos criar
    cidade=cidade,
    estado=estado
  ))


#listando diaristas por cidade
def listar_diaristas_cidade(cep):
  codigo_ibge = buscar_cidade_cep(cep)['ibge']
  try:
    cidade = CidadesAtendidas.objects.get(codigo_ibge=codigo_ibge) #passado como parametro o código IBGE
    return cidade.usuario.filter(tipo_usuario=2).order_by('-reputacao') #usando filtro e tipo_usuario = 2 e ordenando
  except CidadesAtendidas.DoesNotExist:
    return []
  
#verificando a existencia de uma cidade correspondente ao CEP buscado
def verificar_disponibilidade_cidade(cep):
  codigo_ibge = buscar_cidade_cep(cep)['ibge']
  return CidadesAtendidas.objects.filter(codigo_ibge=codigo_ibge).exists()


#aqui buscamos o usuario apartir do id, limpamos a lista de cidade que ele atende e para cada cidade que estamos enviando atraves do corpo a gente busca essa cidade com o código do ibge, e busca no bancom, se existir ele retorna se não ele cria
def relacionar_cidade_diarista(usuario, cidades):
  usuario_relacionar = listar_usuario_id(usuario.id)
  usuario_relacionar.cidades_atendidas.clear()
  for cidade in cidades.value:
    #aqui temos os dados que retornam da api do IBGE
    dados_api = buscar_cidade_ibge(cidade['codigo_ibge'])
    cidade_nova, create = cadastrar_cidade(cidade['codigo_ibge'], dados_api['nome'], dados_api['microregiao']['mesorregiao']['UF']['sigla'])
    usuario_relacionar.cidades_atendidas.add(cidade_nova.id)


#buscando código IBGE pelo CEP, na api do viacep
def buscar_cidade_cep(cep):
  requisicao = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
  
  if requisicao.status_code == 400:
    raise serializers.ValidationError({"details":"Erro ao buscar CEP!"})
  cidade_api = json.loads(requisicao.content)#estamos captando o conteudo json da API
  if "erro" in cidade_api:
    raise serializers.ValidationError({"details":"CEP informado não existe!"})
  return cidade_api

def buscar_cidade_ibge(ibge):
  requisicao = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{ibge}")
  
  #Aqui fazemos a verificação da API, que se não existir o código IBGE retorna um [], logo tratamos como se a API retorna dois caracteres ([]), retorne um erro
  if len(requisicao.content) == 2:
    raise serializers.ValidationError('A cidade não existe!')
  cidade_api = json.loads(requisicao.content)
  
  return cidade_api