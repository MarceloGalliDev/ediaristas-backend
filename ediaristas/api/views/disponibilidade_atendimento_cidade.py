from rest_framework.views import APIView
from rest_framework.response import Response
from ..services import cidades_atendimento_service
from rest_framework import status as status_http

#aqui estamos retornando um True ou False, onde vai verificar se o CEP tem disponibilidade de atendimento ou não
class DisponibilidadeAtendimentoCidade(APIView):
  def get(self, request, format=None):
    #aqui vamos ter localhost:8000/api/diaristas/disponibilidade?cep={cep}
    cep = self.request.query_params.get('cep', None)
    disponibilidade = cidades_atendimento_service.verificar_disponibilidade_cidade(cep)
    return Response({
      "code": "success",
      "disponibilidade": disponibilidade,
      "message": "Disponibilidade verificada com sucesso",
      "status":status_http.HTTP_200_OK ,
    })