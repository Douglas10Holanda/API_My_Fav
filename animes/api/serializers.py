from rest_framework import serializers
from animes import models

class AnimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Animes
        fields = "__all__"