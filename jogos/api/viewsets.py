from rest_framework import viewsets
from jogos.api import serializers
from jogos import models

class JogosViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.JogosSerializer
    queryset = models.Jogos.objects.all()