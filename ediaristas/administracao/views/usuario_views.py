from ..forms.usuario_forms import UsuarioForm
from django.shortcuts import render
from django.contrib.auth import get_user_model

def cadastrar_usuario(request):
  if request.method == 'POST':
    form_usuario = UsuarioForm(request.POST)
    if form_usuario.is_valid():
      form_usuario.save()
  else:
    form_usuario = UsuarioForm()
  return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

def listar_usuarios(request):
  User = get_user_model()
  usuario = User.objects.all()
  
# Analisa-se dentro da lib a função base UserCreationForm
# Estamos utilizando get_user_model para identificar o tipo de autenticação da api para fazer a validção, assim evitando a quebra da API administrativa em caso de alteração do tipo de authenticação