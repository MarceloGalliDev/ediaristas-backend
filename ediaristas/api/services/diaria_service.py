from ..models import Diaria
from .usuario_service import listar_usuario_id

# passamos um post e aqui recebemos o objeto de acordo com o ID
def listar_diaria_id(diaria_id):
  return Diaria.objects.get(id=diaria_id)

def atualizar_status_diaria(diaria_id, status):
  diaria = listar_diaria_id(diaria_id) #aqui recebemos o id da diaria da função anterior
  diaria.status = status #aqui atualizamos o status, atualizando com o status que recebemos como paramêtro
  diaria.save() #aqui salvamos

def listar_diarias_usuario(usuario_id):
  #usuario logado na aplicação
  usuario = listar_usuario_id(usuario_id)
  #vamos verificar o tipo de usuario
  if usuario.tipo_usuario == 1:
    #vamos retornar da nossa lista de diárias todas as diárias em que atributo cliente é = usuario.id
    return Diaria.objects.filter(cliente=usuario.id).all()
  return Diaria.objects.filter(diariasta=usuario.id).all()
  
  
  
  
# Aqui fazemos os ORM de service, para metodologias de négocios
