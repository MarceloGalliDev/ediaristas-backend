from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..models import EnderecoDiarista
from ..serializers.endereco_diarista_serializer import EnderecoDiaristaSerializer
from ..permissions import diarista_permission


class EnderecoDiarista(APIView):
    #permissao 
    permission_classes = [diarista_permission.DiaristaPermissions, ]
    
    #quando não tivermos um endereço ele vai cadastrar, e se houver ele vai alterar-lo
    def put(self, request, format=None):
        #aqui passamos os dados da nossa requisição
        serializer_endereco_diarista = EnderecoDiaristaSerializer(data=request.data, context={'request': request})
        
        #vamos verificar se esses dados são válidos e se seguem as regras de validação
        if serializer_endereco_diarista.is_valid():
            #persistimos os dados no banco
            serializer_endereco_diarista.save()
            #ele passa como parametro os dados ja validados que é o método validated_data()
            return Response(serializer_endereco_diarista.validated_data, status=status_http.HTTP_201_CREATED)
        return Response(serializer_endereco_diarista.errors, status=status_http.HTTP_400_BAD_REQUEST)