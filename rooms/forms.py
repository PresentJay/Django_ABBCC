from django import forms
from django_countries.fields import CountryField
from . import models


class SearchForm(forms.Form):

    city = forms.CharField(initial="Anywhere")
    country = CountryField(default="KR").formfield()
    room_type = forms.ModelChoiceField(
        required=False, empty_label="Any kind", queryset=models.RoomType.objects.all()
    )
    price = forms.IntegerField(required=False)
    guests = forms.IntegerField(required=False)
    Bedrooms = forms.IntegerField(required=False)
    Beds = forms.IntegerField(required=False)
    Baths = forms.IntegerField(required=False)
    instant_book = forms.BooleanField(required=False)
    superhost = forms.BooleanField(required=False)
    amenities = forms.ModelMultipleChoiceField(
        queryset=models.Amenity.objects.all(), widget=forms.CheckboxSelectMultiple
    )
    facilities = forms.ModelMultipleChoiceField(
        queryset=models.Facility.objects.all(), widget=forms.CheckboxSelectMultiple
    )
