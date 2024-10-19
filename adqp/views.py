from django.shortcuts import render, redirect, get_object_or_404
from .models import regular_user, admin_user, City


def home_page(request):
    # # Query all cities from the database
    # cities = City.objects.all()
    # print(cities)
    # Pass the cities to the template
    return render(request, "adqp/home.html")





from django.http import JsonResponse
from pyspark.sql import SparkSession

def query_db1b_data(request):
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("DB1B Data Query") \
        .getOrCreate()

    # Path to your parquet file
    parquet_input_path = "hdfs://hadoop-master:9000/warehouse/db1b_market_parquet"
    print("Successfully read parquet file")
    # Read the parquet file
    df = spark.read.parquet(parquet_input_path)

    # Register the DataFrame as a temporary SQL table
    df.createOrReplaceTempView("db1b_market")

    # Run a SQL query to filter data by Origin
    sql_query = "SELECT * FROM db1b_market WHERE Origin = 'BOS'"
    result_df = spark.sql(sql_query)

    # Collect the result as a list of dictionaries
    result_data = result_df.toPandas().to_dict(orient="records")

    # Stop the Spark session
    spark.stop()

    # Return the result as JSON response
    return JsonResponse({"results": result_data})



from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

def get_schema_information():
    # Provide the schema information based on models
    # return """
    #     Schema:
    #     1. Table: db1b.market
    #     - id: Auto-increment primary key (Big Integer)
    #     - itin_id: Integer, Itinerary ID
    #     - mkt_id: Integer, Market ID
    #     - mkt_coupons: Integer, Number of Coupons in the Market
    #     - year: Integer, Year
    #     - quarter: Integer, Quarter
    #     - origin_airport_id: Integer, Origin Airport ID
    #     - origin_airport_seq_id: Integer, Origin Airport Sequence ID (airports may change names, new Seq ID for each change)
    #     - origin_city_market_id: Integer, Origin City Market ID
    #     - origin: String, max length 3, Origin Airport Code
    #     - origin_country: String, max length 3, Origin Country (always US)
    #     - origin_state_fips: Integer, Origin State FIPS Code
    #     - origin_state: String, max length 2, Origin State Code (two-letter code)
    #     - origin_state_name: String, max length 100, Full State Name
    #     - origin_wac: Integer, Origin World Area Code
    #     - dest_airport_id: Integer, Destination Airport ID
    #     - dest_airport_seq_id: Integer, Destination Airport Sequence ID (same logic as origin)
    #     - dest_city_market_id: Integer, Destination City Market ID
    #     - dest: String, max length 3, Destination Airport Code
    #     - dest_country: String, max length 3, Destination Country (always US)
    #     - dest_state_fips: Integer, Destination State FIPS Code
    #     - dest_state: String, max length 2, Destination State Code (two-letter code)
    #     - dest_state_name: String, max length 100, Full State Name
    #     - dest_wac: String, max length 3, Destination World Area Code
    #     - airport_group: String, max length 100, Airport Group (groups nearby airports for analysis)
    #     - wac_group: String, max length 100, World Area Code Group (groups by WAC)
    #     - tk_carrier_change: Integer, Ticketing Carrier Change Indicator (1 = Yes)
    #     - tk_carrier_group: String, max length 100, Ticketing Carrier Group
    #     - op_carrier_change: Integer, Operating Carrier Change Indicator (1 = Yes)
    #     - op_carrier_group: String, max length 100, Operating Carrier Group
    #     - rp_carrier: String, max length 3, Reporting Carrier Code
    #     - tk_carrier: String, max length 3, Ticketing Carrier Code for On-line Itineraries
    #     - op_carrier: String, max length 3, Operating Carrier Code for On-line Itineraries
    #     - bulk_fare: Integer, Bulk Fare Indicator (1 = Yes)
    #     - passengers: Integer, Number of Passengers
    #     - mkt_fare: Float, Market Fare (Itinerary Yield * Market Miles Flown)
    #     - mkt_distance: Integer, Market Distance (including ground transport)
    #     - mkt_distance_group: Integer, Distance Group in 500 Mile Intervals
    #     - mkt_miles_flown: Integer, Market Miles Flown (Track Miles)
    #     - non_stop_miles: Integer, Non-Stop Market Miles (using Radian Measure)
    #     - itin_geo_type: Integer, Itinerary Geography Type (1 = Includes non-US, 2 = Domestic only)
    #     - mkt_geo_type: Integer, Market Geography Type (1 = Includes non-US, 2 = Domestic only)
    # """

    return """
        Schema:
        1. Table: db1b.market
        - Id: Auto-increment primary key (Big Integer)
        - ItinId: Integer, Itinerary ID
        - MktId: Integer, Market ID
        - MktCoupons: Integer, Number of Coupons in the Market
        - Year: Integer, Year
        - Quarter: Integer, Quarter
        - OriginAirportId: Integer, Origin Airport ID
        - OriginAirportSeqId: Integer, Origin Airport Sequence ID (airports may change names, new Seq ID for each change)
        - OriginCityMarketId: Integer, Origin City Market ID
        - Origin: String, max length 3, Origin Airport Code
        - OriginCountry: String, max length 3, Origin Country (always US)
        - OriginStateFips: Integer, Origin State FIPS Code
        - OriginState: String, max length 2, Origin State Code (two-letter code)
        - OriginStateName: String, max length 100, Full State Name
        - OriginWac: Integer, Origin World Area Code
        - DestAirportId: Integer, Destination Airport ID
        - DestAirportSeqId: Integer, Destination Airport Sequence ID (same logic as origin)
        - DestCityMarketId: Integer, Destination City Market ID
        - Dest: String, max length 3, Destination Airport Code
        - DestCountry: String, max length 3, Destination Country (always US)
        - DestStateFips: Integer, Destination State FIPS Code
        - DestState: String, max length 2, Destination State Code (two-letter code)
        - DestStateName: String, max length 100, Full State Name
        - DestWac: String, max length 3, Destination World Area Code
        - AirportGroup: String, max length 100, Airport Group (groups nearby airports for analysis)
        - WacGroup: String, max length 100, World Area Code Group (groups by WAC)
        - TkCarrierChange: Integer, Ticketing Carrier Change Indicator (1 = Yes)
        - TkCarrierGroup: String, max length 100, Ticketing Carrier Group
        - OpCarrierChange: Integer, Operating Carrier Change Indicator (1 = Yes)
        - OpCarrierGroup: String, max length 100, Operating Carrier Group
        - RpCarrier: String, max length 3, Reporting Carrier Code
        - TkCarrier: String, max length 3, Ticketing Carrier Code for On-line Itineraries
        - OpCarrier: String, max length 3, Operating Carrier Code for On-line Itineraries
        - BulkFare: Integer, Bulk Fare Indicator (1 = Yes)
        - Passengers: Integer, Number of Passengers
        - MktFare: Float, Market Fare (Itinerary Yield * Market Miles Flown)
        - MktDistance: Integer, Market Distance (including ground transport)
        - MktDistanceGroup: Integer, Distance Group in 500 Mile Intervals
        - MktMilesFlown: Integer, Market Miles Flown (Track Miles)
        - NonStopMiles: Integer, Non-Stop Market Miles (using Radian Measure)
        - ItinGeoType: Integer, Itinerary Geography Type (1 = Includes non-US, 2 = Domestic only)
        - MktGeoType: Integer, Market Geography Type (1 = Includes non-US, 2 = Domestic only)
    """

@csrf_exempt
def text_to_sql_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('input', '')

            prompt = f"""
            You are an experienced data analyst at a company.

            Given the database schema:
            {get_schema_information()}
            
            Convert the following natural language description into an SQL query:
            "{user_input}"
            """

            client = OpenAI(api_key=settings.OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.5
            )

            sql_query = response.choices[0].message.content.strip()
            print(sql_query)

            return JsonResponse({'sql': sql_query}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)

from openai import OpenAI
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

def get_schema_information():
    # Provide the schema information based on models
    # return """
    #     Schema:
    #     1. Table: db1b.market
    #     - id: Auto-increment primary key (Big Integer)
    #     - itin_id: Integer, Itinerary ID
    #     - mkt_id: Integer, Market ID
    #     - mkt_coupons: Integer, Number of Coupons in the Market
    #     - year: Integer, Year
    #     - quarter: Integer, Quarter
    #     - origin_airport_id: Integer, Origin Airport ID
    #     - origin_airport_seq_id: Integer, Origin Airport Sequence ID (airports may change names, new Seq ID for each change)
    #     - origin_city_market_id: Integer, Origin City Market ID
    #     - origin: String, max length 3, Origin Airport Code
    #     - origin_country: String, max length 3, Origin Country (always US)
    #     - origin_state_fips: Integer, Origin State FIPS Code
    #     - origin_state: String, max length 2, Origin State Code (two-letter code)
    #     - origin_state_name: String, max length 100, Full State Name
    #     - origin_wac: Integer, Origin World Area Code
    #     - dest_airport_id: Integer, Destination Airport ID
    #     - dest_airport_seq_id: Integer, Destination Airport Sequence ID (same logic as origin)
    #     - dest_city_market_id: Integer, Destination City Market ID
    #     - dest: String, max length 3, Destination Airport Code
    #     - dest_country: String, max length 3, Destination Country (always US)
    #     - dest_state_fips: Integer, Destination State FIPS Code
    #     - dest_state: String, max length 2, Destination State Code (two-letter code)
    #     - dest_state_name: String, max length 100, Full State Name
    #     - dest_wac: String, max length 3, Destination World Area Code
    #     - airport_group: String, max length 100, Airport Group (groups nearby airports for analysis)
    #     - wac_group: String, max length 100, World Area Code Group (groups by WAC)
    #     - tk_carrier_change: Integer, Ticketing Carrier Change Indicator (1 = Yes)
    #     - tk_carrier_group: String, max length 100, Ticketing Carrier Group
    #     - op_carrier_change: Integer, Operating Carrier Change Indicator (1 = Yes)
    #     - op_carrier_group: String, max length 100, Operating Carrier Group
    #     - rp_carrier: String, max length 3, Reporting Carrier Code
    #     - tk_carrier: String, max length 3, Ticketing Carrier Code for On-line Itineraries
    #     - op_carrier: String, max length 3, Operating Carrier Code for On-line Itineraries
    #     - bulk_fare: Integer, Bulk Fare Indicator (1 = Yes)
    #     - passengers: Integer, Number of Passengers
    #     - mkt_fare: Float, Market Fare (Itinerary Yield * Market Miles Flown)
    #     - mkt_distance: Integer, Market Distance (including ground transport)
    #     - mkt_distance_group: Integer, Distance Group in 500 Mile Intervals
    #     - mkt_miles_flown: Integer, Market Miles Flown (Track Miles)
    #     - non_stop_miles: Integer, Non-Stop Market Miles (using Radian Measure)
    #     - itin_geo_type: Integer, Itinerary Geography Type (1 = Includes non-US, 2 = Domestic only)
    #     - mkt_geo_type: Integer, Market Geography Type (1 = Includes non-US, 2 = Domestic only)
    # """


    return """
        Schema:
        1. Table: db1b.market
        - Id: Auto-increment primary key (Big Integer)
        - ItinId: Integer, Itinerary ID
        - MktId: Integer, Market ID
        - MktCoupons: Integer, Number of Coupons in the Market
        - Year: Integer, Year
        - Quarter: Integer, Quarter
        - OriginAirportId: Integer, Origin Airport ID
        - OriginAirportSeqId: Integer, Origin Airport Sequence ID (airports may change names, new Seq ID for each change)
        - OriginCityMarketId: Integer, Origin City Market ID
        - Origin: String, max length 3, Origin Airport Code
        - OriginCountry: String, max length 3, Origin Country (always US)
        - OriginStateFips: Integer, Origin State FIPS Code
        - OriginState: String, max length 2, Origin State Code (two-letter code)
        - OriginStateName: String, max length 100, Full State Name
        - OriginWac: Integer, Origin World Area Code
        - DestAirportId: Integer, Destination Airport ID
        - DestAirportSeqId: Integer, Destination Airport Sequence ID (same logic as origin)
        - DestCityMarketId: Integer, Destination City Market ID
        - Dest: String, max length 3, Destination Airport Code
        - DestCountry: String, max length 3, Destination Country (always US)
        - DestStateFips: Integer, Destination State FIPS Code
        - DestState: String, max length 2, Destination State Code (two-letter code)
        - DestStateName: String, max length 100, Full State Name
        - DestWac: String, max length 3, Destination World Area Code
        - AirportGroup: String, max length 100, Airport Group (groups nearby airports for analysis)
        - WacGroup: String, max length 100, World Area Code Group (groups by WAC)
        - TkCarrierChange: Integer, Ticketing Carrier Change Indicator (1 = Yes)
        - TkCarrierGroup: String, max length 100, Ticketing Carrier Group
        - OpCarrierChange: Integer, Operating Carrier Change Indicator (1 = Yes)
        - OpCarrierGroup: String, max length 100, Operating Carrier Group
        - RpCarrier: String, max length 3, Reporting Carrier Code
        - TkCarrier: String, max length 3, Ticketing Carrier Code for On-line Itineraries
        - OpCarrier: String, max length 3, Operating Carrier Code for On-line Itineraries
        - BulkFare: Integer, Bulk Fare Indicator (1 = Yes)
        - Passengers: Integer, Number of Passengers
        - MktFare: Float, Market Fare (Itinerary Yield * Market Miles Flown)
        - MktDistance: Integer, Market Distance (including ground transport)
        - MktDistanceGroup: Integer, Distance Group in 500 Mile Intervals
        - MktMilesFlown: Integer, Market Miles Flown (Track Miles)
        - NonStopMiles: Integer, Non-Stop Market Miles (using Radian Measure)
        - ItinGeoType: Integer, Itinerary Geography Type (1 = Includes non-US, 2 = Domestic only)
        - MktGeoType: Integer, Market Geography Type (1 = Includes non-US, 2 = Domestic only)
    """

@csrf_exempt
def text_to_sql_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_input = data.get('input', '')

            prompt = f"""
            You are an experienced data analyst at a company.

            Given the database schema:
            {get_schema_information()}
            
            Convert the following natural language description into an SQL query:
            "{user_input}"

            When returning, because we are going to directly use this returned sql code 
            for querying the data, you need to be aware of string problem, so no change line,
            or other weird text for sql code. Escape single quotes, no need for explicit, etc.
            To handle special characters, such as newline characters (\n) and single quotes ('), in a terminal using curl, you need to properly escape them. In your case, the newline (\n) and single quotes (') in the SQL string need to be escaped correctly for the terminal.

            """

            client = OpenAI(api_key=settings.OPENAI_API_KEY)

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": prompt}
                ],
                max_tokens=150,
                temperature=0.5
            )

            sql_query = response.choices[0].message.content.strip()
            print(sql_query)

            return JsonResponse({'sql': sql_query}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)