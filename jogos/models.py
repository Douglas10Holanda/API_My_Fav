from django.db import models
from categorias.models import Categorias

class Jogos(models.Model):
    titulo = models.CharField(max_length=255)
    produtora = models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    joguei = models.BooleanField()
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='categorias_jogos')

    def __str__(self):
        return self.titulo