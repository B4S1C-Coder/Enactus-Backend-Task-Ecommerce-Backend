from django.db import models
from django.core.validators import RegexValidator

class Supplier(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    # phone number to be stored as eg. +918-12345678901234567
    phone_number = models.CharField(max_length=22, validators=[
        RegexValidator(regex=r"^\+\d{1,4}-\d{6,20}$",
        message="Invalid format or phone number",
        code="invalid_phone_no"),
    ])
