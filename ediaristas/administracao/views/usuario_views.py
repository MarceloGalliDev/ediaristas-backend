from django.shortcuts import render, redirect
from ..forms.usuario_forms import UsuarioForm
from django.contrib.auth import get_user_model

def cadastrar_usuario(request):
  if request.method == 'POST':
    form_usuario = UsuarioForm(request.POST)
    if form_usuario.is_valid():
      form_usuario.save()
      return redirect('listar_usuarios')
  else:
    form_usuario = UsuarioForm()
  return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

def listar_usuarios(request):
  User = get_user_model()
  usuarios = User.objects.filter(is_superuser=True)
  return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})

# Analisa-se dentro da lib a função base UserCreationForm
# Estamos utilizando get_user_model para identificar o tipo de autenticação da api para fazer a validção, assim evitando a quebra da API administrativa em caso de alteração do tipo de authenticação
# User = get_user_model(), aqui estsamos pegando o modo de authenticação do sistema