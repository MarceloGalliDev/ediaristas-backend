from rest_framework.views import APIView 
from rest_framework.response import Response
from ..models import Usuario
from ..serializers.diaristas_localidade_serializer import DiaristasLocalidadesSerializer
from rest_framework import status as status_http
from ..services import cidades_atendimento_service

class DiaristasLocalidades(APIView):
  def get(self, request, format=None):
    cep = self.request.query_params.get('cep', None)
    cidade = cidades_atendimento_service.buscar_cidade_cep(cep)
    print(cidade)
    diaristas = Usuario.objects.filter(tipo_usuario=2)#aqui temos uma lista de diaristas, pelo filtro = 2
    serializer_diaristas_localidade = DiaristasLocalidadesSerializer(diaristas, many=True)
    return Response(serializer_diaristas_localidade.data, status=status_http.HTTP_200_OK)
 