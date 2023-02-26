from django.shortcuts import render, redirect
from ..forms.usuario_forms import CadastroUsuarioForm, EditarUsuarioForm
from django.contrib.auth import get_user_model
from django.contrib import messages 

def cadastrar_usuario(request):
  if request.method == 'POST':
    form_usuario = CadastroUsuarioForm(request.POST)
    if form_usuario.is_valid():
      form_usuario.save()
      messages.info(request, 'Usuário criado com sucesso!')
      return redirect('listar_usuarios')
  else:
    form_usuario = CadastroUsuarioForm()
  return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

def listar_usuarios(request):
  User = get_user_model()
  usuarios = User.objects.filter(is_superuser=True)
  return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

def editar_usuario(request, id):
  User = get_user_model()
  usuario = User.objects.get(id=id)
  form_usuario = EditarUsuarioForm(request.POST or None, instance=usuario)
  if form_usuario.is_valid():
    form_usuario.save()
    messages.info(request, 'Usuário alterado com sucesso!')
    return redirect('listar_usuarios') 
  return render(request, 'usuarios/editar_usuario.html', {'form_usuario': form_usuario})  
  
  
  
# Analisa-se dentro da lib a função base UserCreationForm
# Estamos utilizando get_user_model para identificar o tipo de autenticação da api para fazer a validção, assim evitando a quebra da API administrativa em caso de alteração do tipo de authenticação
# User = get_user_model(), aqui estsamos pegando o modo de authenticação do sistema