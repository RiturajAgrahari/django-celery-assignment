from django.urls import path
from . import views


"""Handling App URLs"""

urlpatterns = [
    path("", views.homepage, name="home page"),
    path("history/", views.history, name="history")
]