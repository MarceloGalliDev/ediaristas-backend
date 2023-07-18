from rest_framework import serializers

class RelacionarCidadeDiaristaSerializer(serializers.Serialier):
    cidades = serializers.ListField(required=False)