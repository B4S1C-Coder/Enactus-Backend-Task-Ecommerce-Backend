from django.db import models
from django.core.validators import MinValueValidator

from rest_api_suppliers.models import Supplier

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    # Ensure that prices are positive values
    price = models.DecimalField(max_digits=10, decimal_places=2,
                    validators=[MinValueValidator(0)])
    material_composition = models.CharField(max_length=200)
    performance_specifications = models.CharField(max_length=200)
    inventory_level = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_image = models.ImageField(upload_to="product_photos/", null=True, blank=True)
