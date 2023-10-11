from django.core.management.base import BaseCommand
from base.models import Product
from base.products import products

class Command(BaseCommand):
    help = 'Import products into the database'

    def handle(self, *args, **options):
        for product_data in products:
            Product.objects.create(**product_data)
            self.stdout.write(self.style.SUCCESS(f'Successfully imported product with _id: {product_data["_id"]}'))
