from rest_framework import serializers
from pessoas import models

class PessoasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoas
        fields = "__all__"