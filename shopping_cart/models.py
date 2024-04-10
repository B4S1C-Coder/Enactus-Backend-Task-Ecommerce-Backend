from django.db import models
from django.contrib.auth.models import User

from rest_api_products.models import Product

class ShoppingCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def total_value(self):
        total = 0

        for item in self.shoppingcartitem_set.all():
            total += item.total_price()
        
        return total

    def checkIfItemID_isAssociated(self, id):
        for item in self.shoppingcartitem_set.all():
            if item.id == id:
                return item
        
        return False

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        self.total_value()

class ShoppingCartItem(models.Model):
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_value(self):
        return self.product.price * self.quantity

        