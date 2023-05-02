from rest_framework import serializers

#Usamos o base, pois nao temos um model para a baseURL, vem direto da API, por isso vamos somente reoganizar as informações
#Estamos subscrevendo o to_representation
class EnderecoCepSerializer(serializers.BaseSerializer):
  def to_representation(self, instance):
    return {
      'cep': instance['cep'],
      'localidade': instance['localidade'],
      'bairro': instance['bairro'],
      'logradouro': instance['logradouro'],
      'uf': instance['uf'],
      'complemento': instance['complemento'],
      'ibge': instance['ibge'],
    }

