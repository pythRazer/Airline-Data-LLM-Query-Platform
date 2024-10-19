# Generated by Django 5.1.1 on 2024-10-10 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("adqp", "0002_alter_marketfields_itin_id_alter_marketfields_mkt_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="marketfields",
            name="airport_group",
            field=models.CharField(help_text="Airport Group", max_length=100),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="bulk_fare",
            field=models.FloatField(help_text="Bulk Fare Indicator (1=Yes)"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="dest_airport_seq_id",
            field=models.IntegerField(
                help_text="Destination Airport, Airport Sequence ID"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="dest_state",
            field=models.CharField(
                help_text="Destination Airport, State Code", max_length=2
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="dest_state_fips",
            field=models.IntegerField(help_text="Destination Airport, State FIPS Code"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="dest_state_name",
            field=models.CharField(
                help_text="Destination State Name 完整州名", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="itin_geo_type",
            field=models.IntegerField(help_text="Itinerary Geography Type"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="mkt_distance",
            field=models.FloatField(
                help_text="Market Distance (Including Ground Transport)"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="mkt_distance_group",
            field=models.IntegerField(
                help_text="Distance Group, in 500 Mile Intervals"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="mkt_fare",
            field=models.FloatField(help_text="Market Fare"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="mkt_geo_type",
            field=models.IntegerField(help_text="Market Geography Type"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="mkt_miles_flown",
            field=models.FloatField(help_text="Market Miles Flown"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="non_stop_miles",
            field=models.FloatField(help_text="Non-Stop Market Miles"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="op_carrier",
            field=models.CharField(help_text="Operating Carrier Code", max_length=3),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="op_carrier_change",
            field=models.FloatField(
                help_text="Operating Carrier Change Indicator (1=Yes)"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="op_carrier_group",
            field=models.CharField(help_text="Operating Carrier Group", max_length=100),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="origin_airport_id",
            field=models.IntegerField(
                help_text="Origin Airport, Airport ID 出發機場ID"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="origin_airport_seq_id",
            field=models.IntegerField(help_text="Origin Airport, Airport Sequence ID"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="origin_city_market_id",
            field=models.IntegerField(
                help_text="Origin Airport, City Market ID 出發城市ID"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="origin_state_name",
            field=models.CharField(
                help_text="Origin State Name 完整州名", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="passengers",
            field=models.FloatField(help_text="Number of Passengers 乘客人數"),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="rp_carrier",
            field=models.CharField(help_text="Reporting Carrier Code", max_length=3),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="tk_carrier",
            field=models.CharField(help_text="Ticketing Carrier Code", max_length=3),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="tk_carrier_change",
            field=models.FloatField(
                help_text="Ticketing Carrier Change Indicator (1=Yes)"
            ),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="tk_carrier_group",
            field=models.CharField(help_text="Ticketing Carrier Group", max_length=100),
        ),
        migrations.AlterField(
            model_name="marketfields",
            name="wac_group",
            field=models.CharField(help_text="World Area Code Group", max_length=100),
        ),
    ]