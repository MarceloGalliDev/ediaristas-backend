# pylint: disable=all
# flake8: noqa

from rest_framework import serializers
from ..models import Diaria, Usuario
from django.db import models
from django.urls import reverse
from administracao.services import servico_service
from ..services.cidades_atendimento_service import verificar_disponibilidade_cidade, buscar_cidade_ibge
from ..hateoas import Hateoas
from django.utils import timezone

class UsuarioDiariaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Usuario
    fields = ('nome_completo', 'nascimento', 'telefone', 'tipo_usuario', 'reputacao', 'foto_usuario')

class DiariaSerializer(serializers.ModelSerializer):
  #campo apenas leitura
  cliente = UsuarioDiariaSerializer(read_only=True)
  valor_comissao = serializers.DecimalField(read_only=True, max_digits=5, decimal_places=2)
  links = serializers.SerializerMethodField(required=False)
  class Meta:
    #model ele valida os dados de acordo com o model Diaria la no models.py
    model = Diaria
    #todos os campos são válidados
    fields = '__all__'
  
  #vamos subscrever o metodo create()
  def create(self, validated_data):
    #aqui pegamos o id do servico
    servico = servico_service.listar_servico_id(validated_data['servico'].id)
    #aqui pegamos o valor da comissao do servico
    valor_comissao = validated_data['preco'] * (servico.porcentagem_comissao / 100 )
    #aqui pegamos o usuario logado pelo context da requisição
    diaria = Diaria.objects.create(valor_comissao=valor_comissao, cliente_id=self.context['request'].user.id, **validated_data)
    return diaria
  
  #validação de localização, se há diária para aquela área (CEP)
  #vamos subscrever o metodo validate, recebendo o self e a diaria=attrs, attrs são os atributos da requisição, valida os attrs em geral, é chamado sempre que for chamado a diária
  def validate(self, attrs):
    if not verificar_disponibilidade_cidade(attrs['cep']):
      raise serializers.ValidationError('Não há diaristas para o CEP informado!')
    qtd_comodos = attrs['quantidade_quartos'] + attrs['quantidade_salas'] + attrs['quantidade_cozinhas'] + \
      attrs['quantidade_banheiros'] + attrs['quantidade_quintais'] + attrs['quantidade_outros']
    if qtd_comodos == 0:
      raise serializers.ValidationError('A diária deve ter pelo menos 1 cômodo selecionado!')
    return attrs
  
  #aqui validamos o código do IBGE para verificar se existe
  def validate_codigo_ibge(self, codigo_ibge):
    buscar_cidade_ibge(codigo_ibge)
    return codigo_ibge
  
  def validate_preco(self, preco):
    servico = servico_service.listar_servico_id(self.initial_data['servico'])
    if servico is None:
      raise serializers.ValidationError('Serviço não existe!')
    valor_total = 0
    valor_total += servico.valor_quarto * self.initial_data['quantidade_quartos']
    valor_total += servico.valor_sala * self.initial_data['quantidade_salas']
    valor_total += servico.valor_cozinha * self.initial_data['quantidade_cozinhas']
    valor_total += servico.valor_banheiro * self.initial_data['quantidade_banheiros']
    valor_total += servico.valor_quintal * self.initial_data['quantidade_quintais']
    valor_total += servico.valor_outros * self.initial_data['quantidade_outros']
    
    if preco == valor_total or preco == servico.valor_minimo:
      if valor_total >= servico.valor_minimo:
        return preco
      return servico.valor_minimo
    raise serializers.ValidationError('Valores não correspondem!')
  
  def validate_tempo_atendimento(self, tempo_atendimento):
    servico = servico_service.listar_servico_id(self.initial_data['servico'])
    if servico is None:
      raise serializers.ValidationError('Serviço não existe!')
    horas_total = 0
    horas_total += servico.horas_quarto * self.initial_data['quantidade_quartos']
    horas_total += servico.horas_sala * self.initial_data['quantidade_salas']
    horas_total += servico.horas_cozinha * self.initial_data['quantidade_cozinhas']
    horas_total += servico.horas_banheiro * self.initial_data['quantidade_banheiros']
    horas_total += servico.horas_quintal * self.initial_data['quantidade_quintais']
    horas_total += servico.horas_outros * self.initial_data['quantidade_outros']
    if tempo_atendimento != horas_total:
      raise serializers.ValidationError('Valores não correspondem!')
    return tempo_atendimento 
  
  def validate_data_atendimento(self, data_atendimento):
    if data_atendimento.hour < 6:
      raise serializers.ValidationError('Horário de início não pode ser menor que 6:00am')
    if (data_atendimento.hour + self.initial_data['tempo_atendimento']) > 22:
      raise serializers.ValidationError('O horário de atendimento não pode passar das 22:00pm')
    if data_atendimento <= (timezone.now() + timezone.timedelta(hours=48)):#aqui estamos pegando a hora atual e adicionando 48 horas
      raise serializers.ValidationError('A data de atendimento não pode ser menor que 48h antes da data atual!') 
    return data_atendimento
  
  def get_links(self, obj):
    usuario = self.context['request'].user
    links = Hateoas()
    if obj.status == 1:
      if usuario.tipo_usuario == 1:
        links.add_post('pagar_diaria', reverse('pagamento-diaria-list', kwargs={'diaria_id': obj.id}))
    else:
      #self é referente ao proprio objeto e ao propria diaria
      links.add_get('self', reverse('diaria-detail', kwargs={'diaria_id': obj.id}))
    return links.to_array()