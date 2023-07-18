from rest_framework import serializers
from ..models import EnderecoDiarista

class EnderecoDiaristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnderecoDiarista
        #pegaremos os campos menos o que está dentro do exclude
        #vamos tratar a parte de requisição e quando formos pegar o endereço através do token de acesso, \
            # vamos subscrever o método create() para pegar esse endereço e relacionar com o endereço de diarista e incluir no banco
        exclude = ['usuario', ]
    
    #estamos subscrevendo o método create()
    def create(self, validated_data):
        #usuario do contexto
        usuario = self.context['request'].user
        #método update_or_create, se ja existir um relacionamento entre as tabelas, ele vai atualizar se nao tiver ele registra no banco
        #ele compara o usuario recebido pela requisição com o os usuarios no banco se ja existir ele atualiza os dados de acordo com o recebido pela requisição
        endereco_diarista = EnderecoDiarista.objects.update_or_create(
            usuario=usuario, defaults=validated_data
        )
        return endereco_diarista