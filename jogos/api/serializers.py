from rest_framework import serializers
from jogos import models

class JogosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Jogos
        fields = "__all__"