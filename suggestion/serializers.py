from rest_framework import serializers
from .models import City


class SuggestionsQuerySerializer(serializers.Serializer):
    q = serializers.CharField()
    latitude = serializers.FloatField(required=False)
    longitude = serializers.FloatField(required=False)


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ["name", "longitude", "latitude"]
