from django import forms
from ..models import Client


class CargarCSVForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "document",
            "first_name",
            "last_name",
        ]
