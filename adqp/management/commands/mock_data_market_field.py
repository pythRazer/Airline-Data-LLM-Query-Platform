from django.core.management.base import BaseCommand
from adqp.models import MarketFields  # Adjust this to the correct model you want to insert data into

class Command(BaseCommand):
    help = "Insert mock data into the MarketFields model"

    def handle(self, *args, **kwargs):
        mock_data = [
            {
                "itin_id": 202143381835, "mkt_id": 20214338183501, "mkt_coupons": 2, "year": 2021, "quarter": 4,
                "origin_airport_id": 10721, "origin_airport_seq_id": 1072102, "origin_city_market_id": 30721,
                "origin": "BOS", "origin_country": "US", "origin_state_fips": 25, "origin_state": "MA",
                "origin_state_name": "Massachusetts", "origin_wac": 13, "dest_airport_id": 10792,
                "dest_airport_seq_id": 1079206, "dest_city_market_id": 30792, "dest": "BUF",
                "dest_country": "US", "dest_state_fips": 36, "dest_state": "NY",
                "dest_state_name": "New York", "dest_wac": "22", "airport_group": "BOS:EWR:BUF",
                "wac_group": "13:21:22", "tk_carrier_change": 0, "tk_carrier_group": "UA:UA",
                "op_carrier_change": 0, "op_carrier_group": "UA:YX", "rp_carrier": "UA", "tk_carrier": "UA",
                "op_carrier": "UA", "bulk_fare": 0, "passengers": 1, "mkt_fare": 293.37, "mkt_distance": 1047,
                "mkt_distance_group": 5, "mkt_miles_flown": 1047, "non_stop_miles": 634, "itin_geo_type": 2,
                "mkt_geo_type": 2
            },
            {
                "itin_id": 202143381836, "mkt_id": 20214338183602, "mkt_coupons": 2, "year": 2021, "quarter": 4,
                "origin_airport_id": 10722, "origin_airport_seq_id": 1072203, "origin_city_market_id": 30722,
                "origin": "LAX", "origin_country": "US", "origin_state_fips": 6, "origin_state": "CA",
                "origin_state_name": "California", "origin_wac": 24, "dest_airport_id": 10892,
                "dest_airport_seq_id": 1089207, "dest_city_market_id": 30892, "dest": "JFK",
                "dest_country": "US", "dest_state_fips": 34, "dest_state": "NY",
                "dest_state_name": "New York", "dest_wac": "32", "airport_group": "LAX:SFO:JFK",
                "wac_group": "24:32:33", "tk_carrier_change": 0, "tk_carrier_group": "AA:AA",
                "op_carrier_change": 0, "op_carrier_group": "AA:XY", "rp_carrier": "AA", "tk_carrier": "AA",
                "op_carrier": "AA", "bulk_fare": 1, "passengers": 2, "mkt_fare": 423.57, "mkt_distance": 2500,
                "mkt_distance_group": 6, "mkt_miles_flown": 2499, "non_stop_miles": 1400, "itin_geo_type": 2,
                "mkt_geo_type": 2
            },
            {
                "itin_id": 202143381837, "mkt_id": 20214338183703, "mkt_coupons": 3, "year": 2022, "quarter": 1,
                "origin_airport_id": 10800, "origin_airport_seq_id": 1080001, "origin_city_market_id": 30800,
                "origin": "SFO", "origin_country": "US", "origin_state_fips": 6, "origin_state": "CA",
                "origin_state_name": "California", "origin_wac": 14, "dest_airport_id": 10950,
                "dest_airport_seq_id": 1095003, "dest_city_market_id": 30950, "dest": "LGA",
                "dest_country": "US", "dest_state_fips": 36, "dest_state": "NY",
                "dest_state_name": "New York", "dest_wac": "22", "airport_group": "SFO:LAX:LGA",
                "wac_group": "14:32:22", "tk_carrier_change": 1, "tk_carrier_group": "UA:AA",
                "op_carrier_change": 1, "op_carrier_group": "UA:BA", "rp_carrier": "UA", "tk_carrier": "UA",
                "op_carrier": "UA", "bulk_fare": 0, "passengers": 1, "mkt_fare": 500.25, "mkt_distance": 3000,
                "mkt_distance_group": 7, "mkt_miles_flown": 2995, "non_stop_miles": 1700, "itin_geo_type": 1,
                "mkt_geo_type": 1
            }
        ]
        for data in mock_data:
            MarketFields.objects.create(**data)
        self.stdout.write(self.style.SUCCESS('Successfully inserted mock data!'))
