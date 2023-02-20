# Arquivo para renderizar nossos dados
from django.shortcuts import render, redirect
from ..forms.servico_forms import ServicoForm
from ..models import Servico

def cadastrar_servico(request):
  if request.method == "POST":
    form_servico = ServicoForm(request.POST)# Aqui criamos a instância carregando os dados da request POST, se não tiver nada ele carrega vazio
    if form_servico.is_valid():
      form_servico.save()
      return redirect('listar_servicos')
  else:
    form_servico = ServicoForm() #instaciando um formulário vazio
  return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})

def listar_servicos(request):
  servicos = Servico.objects.all()# é o mesmo que SELECT * FROM servicos
  return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})#{'servicos': servicos} aqui estamos enviando para nosso template com esse variável{'nome da variável': variável referida no self}

def editar_servico(request, id): # Aqui vamos receber a request e o id que queremos editar
  servico = Servico.objects.get(id=id) # Selecionamos o id do form
  form_servico = ServicoForm(request.POST or None, instance=servico)# Aqui estamos fazendo a inclusão da edição, e se caso for somente abertura, adicionamos um None, e a parte do instance é para instanciarmos nosso formulário com os dados já preenchido
  if form_servico.is_valid():
    form_servico.save()
    return redirect('listar_servicos')
  return render(request, 'servicos/form_servico.html', {'form_servico': form_servico})# form_servico: form_servico é usado o mesmo nome do formulário para renderizar os input
  