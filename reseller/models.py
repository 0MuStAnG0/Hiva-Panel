# reseller/models.py

from django.db import models
from django.contrib.auth.models import User

class Reseller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    limit_users = models.PositiveIntegerField(default=10)
    limit_traffic_gb = models.PositiveIntegerField(default=500)
    created_at = models.DateTimeField(auto_now_add=True)

class ResellerUser(models.Model):
    reseller = models.ForeignKey(Reseller, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    expire_date = models.DateField()
    traffic_gb = models.PositiveIntegerField(default=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
