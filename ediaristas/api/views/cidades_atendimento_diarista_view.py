from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as status_http
from ..serializers import cidades_atendimento_diarista_serializer, relacionar_cidade_diarista_serializer
from ..services import usuario_service, cidades_atendimento_service
from ..permissions import diarista_permission

class CidadesAtendimentoDiaristaID(APIView):
    permission_classes = [diarista_permission.DiaristaPermissions, ]
    def put(self, request, format=None):
        #vamos verificar se o array de cidades está sendo enviado, relacionamos os dados da nossa requisição com o serializer
        serializer_cidades_atendimento = relacionar_cidade_diarista_serializer.RelacionarCidadeDiaristaSerializer(data=request.data)
        usuario = usuario_service.listar_usuario_id(request.user.id)
        #verificamos se é valido o array de cidades, se estamos recebendo
        if serializer_cidades_atendimento.is_valid():
            #aqui pegamos a lista de cidades
            cidades = serializer_cidades_atendimento['cidades']
            cidades_atendimento_service.relacionar_cidade_diarista(usuario, cidades)
            return Response(serializer_cidades_atendimento.data, status=status_http.HTTP_201_CREATED)
        return Response(serializer_cidades_atendimento.errors, status=status_http.HTTP_400_BAD_REQUEST)
    

#aqui estamos fazendo a inclusão de cidades atendidas pelos usuarios
#usuario logado: token
#cidades : [
#   '123123123',
#   '321321321
#]