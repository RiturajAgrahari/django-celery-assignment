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
        return render(request, "home.html", {"form": form, "images": []})

    """Here we will handle the page requested by the user with prompt."""
    if request.method == "POST":
        prompt = request.POST.get("prompt")  # extracting the user's prompt
        search_prompt = SearchPrompt.objects.create(search_prompt=prompt)  # adding the prompt to database so that we have a record history

        """Here are 3 celery working extracting images parallaly through API as requested!"""
        image_url1 = generate_images.delay(prompt, search_prompt.id)  # celery worker 1
        image_url2 = generate_images.delay(prompt, search_prompt.id)  # celery worker 2
        image_url3 = generate_images.delay(prompt, search_prompt.id)  # celery worker 3

        # Getting the generated images

        return render(request, "home.html", {"form": form, "images": [image_url1, image_url2, image_url3]})


def history(request, *args, **kwargs):
    """Here we will handle the users records, with the images associated with the prompts"""
    context = {
        "data": {}
    }
    prompts = SearchPrompt.objects.all().values()
    for prompt in prompts:
        images = GeneratedImage.objects.all().filter(search_id=prompt.get("id")).values()
        context["data"][prompt.get("search_prompt")] = images

    return render(request, 'history.html', context=context)
