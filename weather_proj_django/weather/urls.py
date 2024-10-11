from django.urls import path

from . import views

urlpatterns = [
    path("", views.LA_view, name="LA_view"),
]