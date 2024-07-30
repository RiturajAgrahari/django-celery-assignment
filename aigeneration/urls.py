from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="home page"),
    path("generate-image/", views.generate_image, name="generate image")
]