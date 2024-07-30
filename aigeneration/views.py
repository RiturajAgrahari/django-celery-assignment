from django.shortcuts import render, HttpResponse

# Create your views here.


def homepage(request):
    return render(request, "home.html")


def generate_image(request, *args, **kwargs):
    return HttpResponse("we are processing!")