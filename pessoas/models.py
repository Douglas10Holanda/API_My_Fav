from django.db import models
from animes.models import Animes
from filmes.models import Filmes
from series.models import Series
from jogos.models import Jogos

class Pessoas(models.Model):
    nome = models.CharField(max_length=255)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=1)
    series = models.ForeignKey(Series, on_delete=models.CASCADE, related_name="series")
    filmes = models.ForeignKey(Filmes, on_delete=models.CASCADE, related_name="fillmes")
    animes = models.ForeignKey(Animes, on_delete=models.CASCADE, related_name="animes")
    jogos = models.ForeignKey(Jogos, on_delete=models.CASCADE, related_name="jogos")

    def __str__(self):
        return self.nome