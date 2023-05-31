#permissions para um usuario, verificamos se está autenticado e se usuário é dono da diária

from rest_framework import permissions

class ClientePermissions(permissions.BasePermission):
  message = 'Você não possui permissão para acessar este dado.'
  
  def has_permission(self, request, view):
    return request.user and request.user.is_authenticated and request.user.tipo_usuario == 1 # aqui ele precisa ser um usuário, estar autenticado e ser do tipo 1
  
  def has_object_permission(self, request, view, obj):
    return request.user == obj.cliente #aqui comparamos se o user é o mesmo user do objeto