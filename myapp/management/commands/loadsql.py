import json
from decimal import Decimal
from django.core.management.base import BaseCommand
from myapp.models import SQLData

class Command(BaseCommand):
    help = 'Load JSON data into the SQL database'

    def handle(self, *args, **kwargs):
        with open('json_data/stock_market_data.json', 'r') as json_file:
            data = json.load(json_file)
            for entry in data:
                # Remove commas and convert to Decimal for numeric fields
                entry['high'] = Decimal(entry['high'].replace(',', ''))
                entry['low'] = Decimal(entry['low'].replace(',', ''))
                entry['open'] = Decimal(entry['open'].replace(',', ''))
                entry['close'] = Decimal(entry['close'].replace(',', ''))
                entry['volume'] = int(entry['volume'].replace(',', ''))
                SQLData.objects.create(**entry)
        self.stdout.write(self.style.SUCCESS('Successfully loaded JSON data into SQL database'))
