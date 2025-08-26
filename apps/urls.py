from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="app-index"),
    path("navigation/", views.navigation, name="app-navigation"),
]
