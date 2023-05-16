from django.db import models
from django.db.models.aggregates import Avg

class DiaristaManager(models.Manager):
  #Aqui filtramos somente os usuarios do tipo 2 = diaristas
  def get_queryset(self):
    return super().get_queryset().filter(tipo_usuario=2)
  
  #Aqui pegamos a média de todos os usuários
  def reputacao_geral(self):
    return self.get_queryset().all().aggregate(Avg('reputacao'))