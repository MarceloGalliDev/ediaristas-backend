from django import forms
from .models import Servico


class ServicoForm(forms.ModelForm):
#Estamos iniciando uma classe meta, colocando nosso Servico lá de models.py e inicianlizando todos os nossos fields ('__all__') da nossa função
  class Meta:
    model = Servico
    fields = '__all__'