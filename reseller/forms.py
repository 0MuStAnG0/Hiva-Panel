# reseller/forms.py

from django import forms
from .models import ResellerUser

class ResellerUserForm(forms.ModelForm):
    class Meta:
        model = ResellerUser
        fields = ["username", "expire_date", "traffic_gb", "is_active"]
