#POST /api/diaria/pagamento/{id}
#HEADER TOKEN
#BODY CARD_HASH

from rest_framework.views import APIView
from ..services import diaria_service
from ..serializers import pagamento_diaria_serializer
from rest_framework.response import Response
from rest_framework import status as status_http
from ..services.pagamento_diaria_service import realizar_pagamento
from ..permissions import cliente_permission

class PagamentoDiaria(APIView):
  permission_classes = [cliente_permission.ClientePermissions, ]
  
  def post(self, request, diaria_id, formats=None):
    diaria = diaria_service.listar_diaria_id(diaria_id) #buscamos a diaria por id no banco de dados, obtivemos os dados da diária aqui
    self.check_object_permissions(self.request, diaria) #verificamos se a diaria é mesmo do usuario da requisição
    serializer_pagamento = pagamento_diaria_serializer.PagamentoDiariaSerializer(data=request.data) #aqui temos os dados da nossa requisição, e verificamos se ele esta enviando um card_hash
    
    if serializer_pagamento.is_valid(): #aqui verificamos se o campo card_hash esta sendo enviado no corpo da requisição
      card_hash = serializer_pagamento.validated_data['card_hash'] #aqui verificamos se possui card_hash vindo la do front-end
      if diaria.status == 1: #status aqui é do models, se o status for = 1, aqui realizamos o pagamento e retornamos a msg
        realizar_pagamento(diaria, card_hash)
        return Response({'Diária paga com sucesso!'}, status=status_http.HTTP_200_OK)
      return Response({'Não é possível pagar essa diária'}, status=status_http.HTTP_400_BAD_REQUEST)
    return Response(serializer_pagamento.errors, status=status_http.HTTP_400_BAD_REQUEST)