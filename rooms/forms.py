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
        required=False,
        queryset=models.Amenity.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    facilities = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Facility.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ("file", "caption")

    # intercepting save method for add room's primary key on each photo
    def save(self, pk, *args, **kwargs):
        photo = super().save(commit=False)
        room = models.Room.objects.get(pk=pk)
        photo.room = room
        photo.save()


class CreateRoomForm(forms.ModelForm):
    """Form definition for CreateRoom."""

    class Meta:
        """Meta definition for CreateRoomform."""

        model = models.Room
        fields = (
            "name",
            "description",
            "country",
            "city",
            "price",
            "address",
            "guests",
            "beds",
            "bedrooms",
            "baths",
            "check_in",
            "check_out",
            "instant_book",
            "room_type",
            "amenities",
            "facilities",
            "house_rules",
        )

    # processing in frontend (if you can't get the user )
    def save(self, *args, **kwargs):
        room = super().save(
            commit=False
        )  # if you setting save options with 'commit=False',
        # you can not save many to many fields.
        return room

    # processing in backend (if you can get the user)
    # """ def save(self, user, *args, **kwargs):
    #     room = super().save(commit=False)
    #     room.host = user
    #     room.save() """

