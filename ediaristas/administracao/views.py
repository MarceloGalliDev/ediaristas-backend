# Arquivo para renderizar nossos dados
from django.shortcuts import render
from .forms import ServicoForm

def cadastrar_servico(request):
  if request.method == "POST":
    form_servico = ServicoForm(request.POST)# Aqui criamos a instância carregando os dados da request POST, se não tiver nada ele carrega vazio
    if form_servico.is_valid():
      form_servico.save()
  else:
    form_servico = ServicoForm() #instaciando um formulário vazio
  return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})
