from rest_framework import serializers

class PagamentoDiariaSerializer(serializers.Serializer):
  #gerado pelo gatway do pagar.me
  card_hash = serializers.CharField(required=True)