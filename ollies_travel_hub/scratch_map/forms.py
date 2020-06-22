from django import forms
from django.core import validators
from .models import Trip


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        # fields = ("","")
        # fields = "__all__"
        exclude = ["author"]

        widgets = {
            'year_visited': forms.NumberInput(attrs={
                # 'class': 'form-control',
                'placeholder': 'The year you visited'
            }),
            'note': forms.Textarea(attrs={
                # 'class': 'form-control',
                'placeholder': 'Some things you remember...'
            }),
        }
