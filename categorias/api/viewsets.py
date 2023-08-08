from rest_framework import viewsets
from categorias.api import serializers
from categorias import models

class CategoriasViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriasSerializer
    queryset = models.Categorias.objects.all()