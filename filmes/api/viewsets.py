from rest_framework import viewsets
from filmes.api import serializers
from filmes import models

class FilmesViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.FilmesSerializer
    queryset = models.Filmes.objects.all()