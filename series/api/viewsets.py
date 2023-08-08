from rest_framework import viewsets
from series.api import serializers
from series import models

class SeriesViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.SeriesSerializer
    queryset = models.Series.objects.all()