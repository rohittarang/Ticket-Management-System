from dataclasses import fields
from django import forms
from .models import Ticket2

class SaveTicket(forms.ModelForm):
    class Meta:
        model = Ticket2
        fields = ['ticket_id','server_details','send_date','license_no','file']
