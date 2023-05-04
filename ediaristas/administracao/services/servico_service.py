from ..models import Servico

def listar_servico():
  return Servico.objects.order_by('posicao')