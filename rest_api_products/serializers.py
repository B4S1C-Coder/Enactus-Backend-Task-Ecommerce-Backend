from rest_framework import serializers
from .models import Product
from rest_api_suppliers.models import Supplier

class ProductSerializer(serializers.ModelSerializer):
    supplierid = serializers.ReadOnlyField(source="supplier.id")
    class Meta:
        model = Product
        fields = "__all__"