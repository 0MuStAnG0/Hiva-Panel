# payments/models.py

from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    METHOD_CHOICES = [
        ("zarinpal", "زرین‌پال"),
        ("cart_to_cart", "کارت به کارت"),
        ("payeer", "Payeer (کریپتو)"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    amount = models.PositiveIntegerField()
    ref_id = models.CharField(max_length=100, blank=True)
    tracking_code = models.CharField(max_length=100, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
