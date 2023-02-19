from django import forms
from .models import Servico
from django.forms import widgets
from decimal import Decimal



class ServicoForm(forms.ModelForm):
  valor_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  class Meta:
    model = Servico
    fields = '__all__'
    
    
#Estamos iniciando uma classe meta, colocando nosso Servico lá de models.py e inicianlizando todos os nossos fields ('__all__') da nossa função.