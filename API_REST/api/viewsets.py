from rest_framework import viewsets
from API_REST.models import Palavra
from .serializers import PalavraSerializer


class PalavraViewSet(viewsets.ModelViewSet):
    queryset = Palavra.objects.all()
    serializer_class = PalavraSerializer
