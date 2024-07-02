
from django.core.management.base import BaseCommand
from base.models import Product

class Command(BaseCommand):
    help = 'Load initial product data'

    def handle(self, *args, **kwargs):
        data = [
            {'product_id': 'P001', 'description': 'First product description', 'price' : 2.00},
            {'product_id': 'P002', 'description': 'Second product description', 'price' : 3.00},
            {'product_id': 'P003', 'description': 'Third product description'},
            {'product_id': 'P004', 'description': 'Fourth product description'},
            {'product_id': 'P005', 'description': 'Fifth product description'},
            {'product_id': 'P006', 'description': 'Sixth product description'},
            {'product_id': 'P007', 'description': 'Seventh product description'},
            {'product_id': 'P008', 'description': 'Eighth product description'},
            {'product_id': 'P009', 'description': 'Nineth product description'},
        ]

        for item in data:
            Product.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('Products loaded successfully'))
