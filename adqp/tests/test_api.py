from django.test import TestCase
from rest_framework.test import APIClient
from adqp.models import City


class CityDataAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create City objects for the test database
        City.objects.create(code=1001, name="New York")
        City.objects.create(code=1002, name="Los Angeles")
        City.objects.create(code=1003, name="Chicago")

    def test_fetch_city_data(self):
        # Use the URL directly
        response = self.client.get('/adqp/api/city-data/')

        # Assert that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Optional: Print status code and response data for debugging
        print("status code: ", response.status_code)
        print("response: ", response.data)  # Raw response data
        print("response JSON: ", response.json())  # JSON serialized response

        # Update the expected data to include the 'id' field
        expected_data = [
            {"id": 1, "code": 1001, "name": "New York"},
            {"id": 2, "code": 1002, "name": "Los Angeles"},
            {"id": 3, "code": 1003, "name": "Chicago"},
        ]

        # Assert the response data matches the expected data
        self.assertEqual(response.json(), expected_data)
