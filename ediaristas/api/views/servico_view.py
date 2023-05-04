from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from administracao.services import servico_service
from ..serializers import servico_serializer

#Buscando todos os serviçoes da api
class Servico(APIView):
  def get(self, request, format=None):
    servicos = servico_service.listar_servico()#consulta do data de servico
    serializer_servico = servico_serializer.ServicoSerializer(servicos, many=True)#aqui é o tratamento dos dados
    return Response(serializer_servico.data, status=status_http.HTTP_200_OK)#aqui retornamos os dados com status