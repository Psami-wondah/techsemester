from rest_framework.test import APITestCase
from .models import City


class SuggestionsTestCase(APITestCase):
    def setUp(self):
        City.objects.create(
            name="Port Harcourt, Nigeria", longitude=22.3, latitude=34.2
        )
        City.objects.create(name="Ikejaport, Nigeria", latitude=32.2, longitude=30.3)

    def test_suggestions_endpoint_returns_searched_data(self):
        response = self.client.get("/api/v1/suggestions?q=Port")
        data = response.json()
        self.assertEqual(data["suggestions"][0]["name"], "Port Harcourt, Nigeria")
        self.assertEqual(data["suggestions"][0]["latitude"], 34.2)

        self.assertEqual(data["suggestions"][1]["name"], "Ikejaport, Nigeria")

    def test_suggestions_endpoint_returns_score(self):
        response = self.client.get(
            "/api/v1/suggestions?q=Port&latitude=43.2&longitude=31.8"
        )
        data = response.json()
        self.assertTrue(data["suggestions"][0]["score"])
