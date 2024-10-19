import os
import subprocess
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType, DoubleType

FILE_NAME = "Origin_and_Destination_Survey_DB1BMarket_2024_1"

def download_and_unzip():
    # URL of the file to download
    url = f"https://transtats.bts.gov/PREZIP/{FILE_NAME}.zip"
    
    # Filename for the downloaded zip file

    # Download the file using wget
    print(f"Downloading {url}...")
    subprocess.run(["wget", url], check=True)

    # Unzip the file
    print(f"Unzipping {FILE_NAME}...")
    subprocess.run(["unzip", FILE_NAME], check=True)

    print("Download and extraction complete!")


if __name__ == "__main__":
    download_and_unzip()

    # Initialize Spark session using Spark Connect
    spark = SparkSession \
        .builder \
        .appName("DB1B Data Ingestion") \
        .master("local") \
        .enableHiveSupport() \
        .getOrCreate()

    # Define the schema based on your provided CSV schema
    schema = StructType([
        StructField("ItinID", LongType(), True),
        StructField("MktID", LongType(), True),
        StructField("MktCoupons", IntegerType(), True),
        StructField("Year", IntegerType(), True),
        StructField("Quarter", IntegerType(), True),
        StructField("OriginAirportID", IntegerType(), True),
        StructField("OriginAirportSeqID", IntegerType(), True),
        StructField("OriginCityMarketID", IntegerType(), True),
        StructField("Origin", StringType(), True),
        StructField("OriginCountry", StringType(), True),
        StructField("OriginStateFips", IntegerType(), True),
        StructField("OriginState", StringType(), True),
        StructField("OriginStateName", StringType(), True),
        StructField("OriginWac", IntegerType(), True),
        StructField("DestAirportID", IntegerType(), True),
        StructField("DestAirportSeqID", IntegerType(), True),
        StructField("DestCityMarketID", IntegerType(), True),
        StructField("Dest", StringType(), True),
        StructField("DestCountry", StringType(), True),
        StructField("DestStateFips", IntegerType(), True),
        StructField("DestState", StringType(), True),
        StructField("DestStateName", StringType(), True),
        StructField("DestWac", IntegerType(), True),
        StructField("AirportGroup", StringType(), True),
        StructField("WacGroup", StringType(), True),
        StructField("TkCarrierChange", DoubleType(), True),
        StructField("TkCarrierGroup", StringType(), True),
        StructField("OpCarrierChange", DoubleType(), True),
        StructField("OpCarrierGroup", StringType(), True),
        StructField("RPCarrier", StringType(), True),
        StructField("TkCarrier", StringType(), True),
        StructField("OpCarrier", StringType(), True),
        StructField("BulkFare", DoubleType(), True),
        StructField("Passengers", DoubleType(), True),
        StructField("MktFare", DoubleType(), True),
        StructField("MktDistance", DoubleType(), True),
        StructField("MktDistanceGroup", IntegerType(), True),
        StructField("MktMilesFlown", DoubleType(), True),
        StructField("NonStopMiles", DoubleType(), True),
        StructField("ItinGeoType", IntegerType(), True),
        StructField("MktGeoType", IntegerType(), True)
    ])

    cwd = os.getcwd()

    csv_path = f"file://{cwd}/Origin_and_Destination_Survey_DB1BMarket_2024_1.csv"

    # Must use file:// prefix to specify local file path
    df = spark.read.csv(csv_path, header=True, schema=schema)

    # Create database if not exists
    spark.sql("CREATE DATABASE IF NOT EXISTS db1b")

    df.write.saveAsTable("db1b.market", mode="overwrite", header=True)

    spark.stop()

    os.remove(f"{FILE_NAME}.zip")
    os.remove(f"{FILE_NAME}.csv")
    os.remove("readme.html")