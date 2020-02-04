from django.utils import timezone
from django.views.generic import ListView, DetailView
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django_countries import countries
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


# Function Based View method
# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         # return redirect(reverse("core:home"))
#         raise Http404()


# Class Based View method (DetailView)
class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


def search(request):
    city = request.GET.get("city", "Anywhere")
    country = request.GET.get("country", "KR")
    room_types = models.RoomType.objects.all()
    room_type = int(request.GET.get("room_type", 0))

    form = {
        "city": city.capitalize(),
        "s_country": country,
        "s_room_type": room_type,
    }

    choices = {
        "countries": countries,
        "room_types": room_types,
    }

    return render(request, "rooms/search.html", {**form, **choices},)
