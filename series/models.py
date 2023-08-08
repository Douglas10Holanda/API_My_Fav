from django.db import models
from categorias.models import Categorias

class Series(models.Model):
    titulo = models.CharField(max_length=255)
    produtora = models.CharField(max_length=100)
    temporadas = models.IntegerField()
    ano_lancamento = models.IntegerField()
    assistiu = models.BooleanField()
    categorias = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='categorias_series')

    def __str__(self):
        return self.titulo