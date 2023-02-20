from django import forms
from .models import Servico
from django.forms import widgets
from decimal import Decimal

class ServicoForm(forms.ModelForm):
  valor_minimo = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  porcentagem_comissao = forms.CharField(widget=forms.TextInput(attrs={'class': 'percent'}))
  valor_quarto = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  valor_sala = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  valor_banheiro = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  valor_cozinha = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  valor_quintal = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  valor_outros = forms.CharField(widget=forms.TextInput(attrs={'class': 'money'}))
  class Meta:
    model = Servico
    fields = '__all__'
  
  def clean_valor_minimo(self):
    data = self.cleaned_data['valor_minimo']
    return Decimal(data.replace(',', '.').replace('R$',''))

  def clean_porcentagem_comissao(self):
    data = self.cleaned_data['porcentagem_comissao']
    return Decimal(data.replace(',', '.').replace('%', ' '))
    
  def clean_valor_quarto(self):
    data = self.cleaned_data['valor_quarto']
    return Decimal(data.replace(',', '.').replace('R$',''))
    
  def clean_valor_sala(self):
    data = self.cleaned_data['valor_sala']
    return Decimal(data.replace(',', '.').replace('R$',''))
    
  def clean_valor_banheiro(self):
    data = self.cleaned_data['valor_banheiro']
    return Decimal(data.replace(',', '.').replace('R$',''))
    
  def clean_valor_cozinha(self):
    data = self.cleaned_data['valor_cozinha']
    return Decimal(data.replace(',', '.').replace('R$',''))
    
  def clean_valor_quintal(self):
    data = self.cleaned_data['valor_quintal']
    return Decimal(data.replace(',', '.').replace('R$',''))
    
  def clean_valor_outros(self):
    data = self.cleaned_data['valor_outros']
    return Decimal(data.replace(',', '.').replace('R$',''))
    
    
# Estamos iniciando uma classe meta, colocando nosso Servico lá de models.py e inicianlizando todos os nossos fields ('__all__') da nossa função.
# valor_minimo, estamos realizando a inclusão da máscara nos inputs com classe money
