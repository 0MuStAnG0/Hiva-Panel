# adminpanel/forms.py

from django import forms
from subscriptions.models import Plan

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'traffic_gb', 'duration_days', 'price']
