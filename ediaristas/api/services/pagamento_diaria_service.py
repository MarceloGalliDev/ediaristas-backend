from ..models import Pagamento
from .diaria_service import atualizar_status_diaria

def realizar_pagamento(diaria, card_hash):
  Pagamento.objects.create(status="pago", #aqui estamos passando o status pago escondido
  valor=diaria.preco, #essa campo esta o models
  transacao_id="12a9daqwe",
  diaria=diaria
  )
  atualizar_status_diaria(diaria.id, 2) #aqui estamos passando os paramêtros para dentro da função
  return