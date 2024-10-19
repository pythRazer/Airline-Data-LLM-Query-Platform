import csv
from django.core.management.base import BaseCommand
from adqp.models import City

class Command(BaseCommand):
    help = 'Import city data from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file to import')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']

        # Open the CSV file
        with open(csv_file, newline='') as file:
            reader = csv.DictReader(file)

            # Iterate over each row in the CSV
            for row in reader:
                code = row['Code']
                name = row['Description']

                # Create or update the City object
                City.objects.update_or_create(
                    code=code,
                    defaults={'name': name}
                )

        self.stdout.write(self.style.SUCCESS(f"Successfully imported city data from {csv_file}"))
