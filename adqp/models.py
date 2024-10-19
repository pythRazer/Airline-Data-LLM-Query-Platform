from django.db import models

class MarketFields(models.Model):
    itin_id = models.BigIntegerField(help_text="Itinerary ID")  # LONG
    mkt_id = models.BigIntegerField(help_text="Market ID")  # LONG
    mkt_coupons = models.IntegerField(help_text="Number of Coupons in the Market")  # INT
    year = models.IntegerField(help_text="Year")  # INT
    quarter = models.IntegerField(help_text="Quarter")  # INT
    origin_airport_id = models.IntegerField(help_text="Origin Airport, Airport ID 出發機場ID")  # INT
    origin_airport_seq_id = models.IntegerField(help_text="Origin Airport, Airport Sequence ID")  # INT
    origin_city_market_id = models.IntegerField(help_text="Origin Airport, City Market ID 出發城市ID")  # INT
    origin = models.CharField(max_length=3, help_text="Origin Airport Code 出發機場代號")  # STRING
    origin_country = models.CharField(max_length=3, help_text="全都是 US")  # STRING
    origin_state_fips = models.IntegerField(help_text="Origin Airport, State FIPS Code 出發州的數字代號")  # INT
    origin_state = models.CharField(max_length=2, help_text="Origin Airport, State Code 出發州的兩碼英文代號")  # STRING
    origin_state_name = models.CharField(max_length=100, help_text="Origin State Name 完整州名")  # STRING
    origin_wac = models.IntegerField(help_text="Origin Airport, World Area Code")  # INT
    dest_airport_id = models.IntegerField(help_text="Destination Airport, Airport ID 抵達機場ID")  # INT
    dest_airport_seq_id = models.IntegerField(help_text="Destination Airport, Airport Sequence ID")  # INT
    dest_city_market_id = models.IntegerField(help_text="Destination Airport, City Market ID 抵達城市ID")  # INT
    dest = models.CharField(max_length=3, help_text="Destination Airport Code 抵達機場代號")  # STRING
    dest_country = models.CharField(max_length=3, help_text="Destination Country 全都是 US")  # STRING
    dest_state_fips = models.IntegerField(help_text="Destination Airport, State FIPS Code")  # INT
    dest_state = models.CharField(max_length=2, help_text="Destination Airport, State Code")  # STRING
    dest_state_name = models.CharField(max_length=100, help_text="Destination State Name 完整州名")  # STRING
    dest_wac = models.CharField(max_length=3, help_text="Destination Airport, World Area Code")  # STRING
    airport_group = models.CharField(max_length=100, help_text="Airport Group")  # STRING
    wac_group = models.CharField(max_length=100, help_text="World Area Code Group")  # STRING
    tk_carrier_change = models.FloatField(help_text="Ticketing Carrier Change Indicator (1=Yes)")  # DOUBLE
    tk_carrier_group = models.CharField(max_length=100, help_text="Ticketing Carrier Group")  # STRING
    op_carrier_change = models.FloatField(help_text="Operating Carrier Change Indicator (1=Yes)")  # DOUBLE
    op_carrier_group = models.CharField(max_length=100, help_text="Operating Carrier Group")  # STRING
    rp_carrier = models.CharField(max_length=3, help_text="Reporting Carrier Code")  # STRING
    tk_carrier = models.CharField(max_length=3, help_text="Ticketing Carrier Code")  # STRING
    op_carrier = models.CharField(max_length=3, help_text="Operating Carrier Code")  # STRING
    bulk_fare = models.FloatField(help_text="Bulk Fare Indicator (1=Yes)")  # DOUBLE
    passengers = models.FloatField(help_text="Number of Passengers 乘客人數")  # DOUBLE
    mkt_fare = models.FloatField(help_text="Market Fare")  # DOUBLE
    mkt_distance = models.FloatField(help_text="Market Distance (Including Ground Transport)")  # DOUBLE
    mkt_distance_group = models.IntegerField(help_text="Distance Group, in 500 Mile Intervals")  # INT
    mkt_miles_flown = models.FloatField(help_text="Market Miles Flown")  # DOUBLE
    non_stop_miles = models.FloatField(help_text="Non-Stop Market Miles")  # DOUBLE
    itin_geo_type = models.IntegerField(help_text="Itinerary Geography Type")  # INT
    mkt_geo_type = models.IntegerField(help_text="Market Geography Type")  # INT

    def __str__(self):
        return f"ItinID: {self.itin_id}, MktID: {self.mkt_id}"


class City(models.Model):
    code = models.IntegerField(default=0)
    name = models.CharField(max_length=64)


# User credentials, one for regular user, one for admin user
regular_user = {"username": "rich",
                "password": "regular"
                }

admin_user = {
    "username": "admin",
    "password": "admin"
}



