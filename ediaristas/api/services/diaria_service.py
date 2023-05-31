from ..models import Diaria

# passamos um post e aqui recebemos o objeto de acordo com o ID
def listar_diaria_id(diaria_id):
  return Diaria.objects.get(id=diaria_id)

def atualizar_status_diaria(diaria_id, status):
  diaria = listar_diaria_id(diaria_id) #aqui recebemos o id da diaria da função anterior
  diaria.status = status #aqui atualizamos o status, atualizando com o status que recebemos como paramêtro
  diaria.save() #aqui salvamos

# Aqui fazemos os ORM de service, para metodologias de négocios
