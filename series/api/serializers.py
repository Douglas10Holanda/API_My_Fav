from rest_framework import serializers
from series import models

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Series
        fields = "__all__"