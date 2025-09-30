from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing

        fields=[
            'title',
            'description',
            'brand',
            'model',
            'city',
            'price',
            'year',
            'mileage',
            'fuel',
            'gearbox',
            'main_image'
        ]

        widgets = {
            'description': forms.Textarea(attrs={'rows':4}),
        }