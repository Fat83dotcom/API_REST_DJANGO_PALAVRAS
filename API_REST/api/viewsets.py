from rest_framework import viewsets
from API_REST.models import Palavra
from .serializers import PalavraSerializer
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


class PalavraViewSet(viewsets.ModelViewSet):
    queryset = Palavra.objects.all()
    serializer_class = PalavraSerializer


# @api_view()
# def qtdPalavras(request):
#     qtd = Palavra.objects.count()
#     return Response(qtd)
