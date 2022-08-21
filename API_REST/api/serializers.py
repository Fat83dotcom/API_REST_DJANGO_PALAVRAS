from rest_framework import serializers
from API_REST.models import Palavra


class PalavraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palavra
        fields = ['id_palavra', 'nome', 'categoria']
