import requests
import json
from rest_framework import serializers
from ..models import CidadesAtendidas

#listando diaristas por cidade
def listar_diaristas_cidade(cep):
  codigo_ibge = buscar_cidade_cep(cep)['ibge']
  try:
    cidade = CidadesAtendidas.objects.get(codigo_ibge=codigo_ibge) #passado como parametro o código IBGE
    return cidade.usuario.filter(tipo_usuario=2).order_by('-reputacao') #usando filtro e tipo_usuario = 2 e ordenando
  except CidadesAtendidas.DoesNotExist:
    return []
  
#buscando código IBGE pelo CEP, na api do viacep
def buscar_cidade_cep(cep):
  requisicao = requests.get(f"http://viacep.com.br/ws/{cep}/json/")
  
  if requisicao.status_code == 400:
    raise serializers.ValidationError({"details":"Erro ao buscar CEP!"})
  cidade_api = json.loads(requisicao.content)#estamos captando o conteudo json da API
  if "erro" in cidade_api:
    raise serializers.ValidationError({"details":"CEP informado não existe!"})
  return cidade_api