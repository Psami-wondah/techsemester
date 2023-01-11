from rest_framework.generics import GenericAPIView
from .serializers import CitySerializer, SuggestionsQuerySerializer
from drf_yasg.utils import swagger_auto_schema
from .models import City
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from utils.utils import distance_between_points


def get_score(max: float, min: float, value: float):
    range = max - min
    value_range = value - min
    if value_range == 0:
        return 0.99
    return abs(round(0.99 - (value_range / range), 2))


class Suggestion(GenericAPIView):
    serializer_class = CitySerializer

    @swagger_auto_schema(query_serializer=SuggestionsQuerySerializer)
    def get(self, request):
        q = request.query_params.get("q")
        if not q:
            return Response(
                {"message": "Please enter search query q", "status": False},
                status=status.HTTP_200_OK,
            )

        cities = City.objects.filter(Q(name__contains=q))
        serializer = self.serializer_class(instance=cities, many=True)
        _cities = serializer.data

        longitude = request.query_params.get("longitude")
        latitude = request.query_params.get("latitude")
        if latitude and longitude:
            latitude = float(latitude)
            longitude = float(longitude)

            distances = list(
                map(
                    lambda city: distance_between_points(
                        lat1=city["latitude"],
                        lng1=city["longitude"],
                        lat2=latitude,
                        lng2=longitude,
                    ),
                    _cities,
                )
            )
            max_distance = max(distances)
            min_distance = min(distances)

            def check_distance(city):
                distance = distance_between_points(
                    lat1=city["latitude"],
                    lng1=city["longitude"],
                    lat2=latitude,
                    lng2=longitude,
                )
                return {
                    **city,
                    "score": get_score(max_distance, min_distance, distance),
                }

            _cities = list(
                map(
                    check_distance,
                    _cities,
                )
            )

        return Response(
            {
                "message": f"{cities.count()} Cities",
                "suggestions": _cities,
                "status": True,
            },
            status=status.HTTP_200_OK,
        )
