
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("atlas/", views.section, {"section_name": "Sector Atlas"}, name="atlas"),
    path("worlds/", views.section, {"section_name": "Worlds"}, name="worlds"),
    path("factions/", views.section, {"section_name": "Factions"}, name="factions"),
    path("characters/", views.section, {"section_name": "Characters"}, name="characters"),
    path("chronicles/", views.section, {"section_name": "Chronicles"}, name="chronicles"),
]
