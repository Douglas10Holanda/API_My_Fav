from django.db import models
from categorias.models import Categorias

class Filmes(models.Model):
    titulo = models.CharField(max_length=255)
    estudio = models.CharField(max_length=100)
    duracao = models.IntegerField()
    ano_lancamento = models.IntegerField()
    assistiu = models.BooleanField()
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='categorias_filmes')


    def __str__(self):
        return self.titulo