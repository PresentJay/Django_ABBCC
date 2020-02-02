from django.urls import path
from rooms import views as room_views

app_name = "core"

urlpatterns = [
    path("", room_views.all_rooms, name="home"),
]

# names of each path must be same with namespace of config.urls!
