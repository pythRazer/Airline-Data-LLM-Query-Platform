from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CitySerializer, MarketFieldsSerializer
from adqp.models import City, MarketFields
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from adqp.models import MarketFields
from django.db import connection
import os
import subprocess
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType, DoubleType

# class CityListView(APIView):
#     def get(self, request, format=None):
#         cities = City.objects.all()
#         serializer = CitySerializer(cities, many=True)
#         return Response(serializer.data)





# from adqp.serializers import MarketFieldsSerializer

class MarketFieldsView(APIView):
    # Retrieve all market fields or a single market field by pk
    def get(self, request, pk=None, format=None):
        if pk:
            try:
                market_field = MarketFields.objects.get(pk=pk)
            except MarketFields.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            serializer = MarketFieldsSerializer(market_field)
            return Response(serializer.data)
        else:
            market_fields = MarketFields.objects.all()
            serializer = MarketFieldsSerializer(market_fields, many=True)
            return Response(serializer.data)

    # Create a new market field (POST)
    def post(self, request, format=None):
        serializer = MarketFieldsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Update an existing market field (PUT)
    def put(self, request, pk, format=None):
        try:
            market_field = MarketFields.objects.get(pk=pk)
        except MarketFields.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = MarketFieldsSerializer(market_field, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a market field (DELETE)
    def delete(self, request, pk, format=None):
        try:
            market_field = MarketFields.objects.get(pk=pk)
        except MarketFields.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        market_field.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class QueryView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract the query from the request body
        query_data = request.data.get('query', None)

        if not query_data:
            return Response({"error": "Query field is required in the request."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Initialize Spark session using Spark Connect
            print("Initializing Spark session...")
            spark = SparkSession \
                .builder \
                .appName("DB1B Data Query") \
                .master("local") \
                .enableHiveSupport() \
                .getOrCreate()



            # Run the SQL query using Spark
            result_df = spark.sql(query_data)

            # Collect the result and convert it to JSON
            result = result_df.collect()
            columns = result_df.columns
            data = [dict(zip(columns, row)) for row in result]

            return Response({"data": data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        finally:
            # Stop the Spark session after the query execution
            spark.stop()
            print("Spark has been stopped.")
