# Arquivo para renderizar nossos dados
from django.shortcuts import render
from .forms import ServicoForm

def cadastrar_servico(request):
  form_servico = ServicoForm() #instaciando um formulário vazio
  return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})
