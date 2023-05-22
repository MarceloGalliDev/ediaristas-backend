from ..models import Servico

def listar_servico():
  return Servico.objects.order_by('posicao')

def listar_servico_id(id_servico):
  return Servico.objects.get(id=id_servico)