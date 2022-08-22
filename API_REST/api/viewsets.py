from rest_framework import viewsets
from API_REST.models import Palavra
from .serializers import PalavraSerializer
from random import randrange


class PalavraViewSet(viewsets.ModelViewSet):
    numeroDeObjetos = Palavra.objects.count()
    objetoEscolhido = randrange(1, numeroDeObjetos)
    queryset = Palavra.objects.all()
    serializer_class = PalavraSerializer
