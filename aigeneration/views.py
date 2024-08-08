from django.shortcuts import render
from .tasks import generate_images
from .forms import PromptForm
from .models import GeneratedImage, SearchPrompt

# Create your views here.


def homepage(request):
    """here we are creating a django form to get text to generate associated images with it"""
    form = PromptForm()

    """Here we will handle the page when it is requested by the user without any prompt"""
    if request.method == "GET":
        images = []

        return render(request, "home.html", {"form": form, "images": images})

    """Here we will handle the page requested by the user with prompt."""
    if request.method == "POST":
        # for key, prompt in request.POST.items():
        #     if key == 'csrfmiddlewaretoken':
        #         continue
        #     else:
        #         image_url = generate_images.delay(prompt)

        """Here are 3 celery working extracting images parallaly through API as requested!"""
        image_url1_id = generate_images.delay(request.POST.get("prompt1"))  # celery worker 1
        image_url2_id = generate_images.delay(request.POST.get("prompt2"))  # celery worker 2
        image_url3_id = generate_images.delay(request.POST.get("prompt3"))  # celery worker 3
        # Getting the generated images

        return render(request, "home.html", {"form": form, "images": []})


def history(request, *args, **kwargs):
    """Here we will handle the users records, with the images associated with the prompts"""
    data = []
    images = GeneratedImage.objects.all().values()
    for image in images:
        data.append(image.get("image"))
    context = {
        "data": data
    }
    return render(request, 'history.html', context=context)
