from rest_framework import serializers
from adqp.models import City, MarketFields

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'
class MarketFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketFields
        fields = '__all__'
