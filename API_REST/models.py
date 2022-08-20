from django.db import models


class Palavras(models.Model):
    id_palavra = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)
    categoria = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nome


class CategoriaPalavra(models.Model):
    nome = models.CharField(primary_key=True, max_length=255)

    def __str__(self) -> str:
        return self.nome
