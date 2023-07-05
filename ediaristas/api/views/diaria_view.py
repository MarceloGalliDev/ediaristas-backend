#vamos verificar o access tokens, se for 1 ou 2

from rest_framework.views import APIView
from ..serializers import diaria_serializer
from ..services.diaria_service import listar_diarias_usuario
from rest_framework.response import Response
from rest_framework import status as status_http
from rest_framework import permissions
from rest_framework import serializers

class Diaria(APIView):
  permission_classes = [permissions.IsAuthenticated, ]
  def post(self, request, format=None):
    #vamos validar a requisição com base no nosso serializer
    #context aqui é para sabermos da onde esta vindo a requisição e seus paramêtros
    serializer_diaria = diaria_serializer.DiariaSerializer(data=request.data, context={'request': request})
    
    if request.user.tipo_usuario == 2:
      raise serializers.ValidationError("Apenas clientes podem solicitar diárias!")
    
    if serializer_diaria.is_valid():
      serializer_diaria.save()
      return Response(serializer_diaria.data, status=status_http.HTTP_201_CREATED)
    return Response(serializer_diaria.errors, status=status_http.HTTP_400_BAD_REQUEST)
  
  def get(self, request, format=None):
    diarias = listar_diarias_usuario(request.user.id)
    #many=True é para indicar que vamos indicar mais de um objeto
    serializer_diaria = diaria_serializer.DiariaSerializer(diarias, many=True, context={'request': request})
    return Response(serializer_diaria.data, status=status_http.HTTP_200_OK)