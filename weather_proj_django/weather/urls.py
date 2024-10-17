from django.urls import path

from . import views

urlpatterns = [
    path("LA_view/", views.LA_view, name="LA_view"),
    path("home_view/", views.home_view, name="home_view"),
]