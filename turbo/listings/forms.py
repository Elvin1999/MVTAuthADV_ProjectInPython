from django import forms
from django.forms import inlineformset_factory

from .models import Listing, ListingImage


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

ListingImageFormSet=inlineformset_factory(
    parent_model=Listing,
    model=ListingImage,
    fields=['image','alt','order'],
    extra=3,
    can_delete=True,
    max_num=10,
    validate_max=True
)