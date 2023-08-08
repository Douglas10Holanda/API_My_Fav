from rest_framework import serializers
from categorias import models

class CategoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categorias
        fields = "__all__"