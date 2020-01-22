from django.contrib import admin
from . import models


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):

    """ Review Admin Definition """

    # if define functions here(admin.py), then it function works only this file

    list_display = ("__str__", "rating_average")

