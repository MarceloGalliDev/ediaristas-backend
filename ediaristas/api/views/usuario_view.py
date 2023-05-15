from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import usuario_serializer
from rest_framework import status as status_http

class Usuario(APIView):
  def post(self, request, format=None):
    serializer_usuario = usuario_serializer.UsuarioSerializer(data=request.data, context={'request': request})
    
    if serializer_usuario.is_valid():
      usuario_criado = serializer_usuario.save()
      serializer_usuario = usuario_serializer.UsuarioSerializer(usuario_criado)
      return Response(usuario_criado.data, status=status_http.HTTP_200_OK)
    return Response(serializer_usuario.errors)
#aqui capturamos os dados vindo do front-end