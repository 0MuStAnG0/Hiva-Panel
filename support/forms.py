# support/forms.py

from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["subject", "message"]

class TicketReplyForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["reply"]
