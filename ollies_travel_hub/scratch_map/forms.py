from django import forms
from django.core import validators
from .models import Trip


class TripForm(forms.ModelForm):

    class Meta:
        model = Trip
        exclude = ["author"]

        widgets = {
            'year_visited': forms.NumberInput(attrs={
                'placeholder': 'The year you visited'
            }),
            'note': forms.Textarea(attrs={
                'placeholder': 'Some things you remember...'
            }),
            'trip_img': forms.ClearableFileInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['country_visited'].label = 'Country Visited'
        self.fields['year_visited'].label = 'Year'
        self.fields['note'].label = 'Note'
        self.fields['trip_img'].label = 'Photo'
