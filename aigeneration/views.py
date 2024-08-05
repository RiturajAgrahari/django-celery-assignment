from django.shortcuts import render
from .tasks import generate_images
from .forms import PromptForm
from .models import GeneratedImage, SearchPrompt
from django.core.cache import cache

# Create your views here.


def homepage(request):
    """here we are creating a django form to get text to generate associated images with it"""
    form = PromptForm()

    """Here we will handle the page when it is requested by the user without any prompt"""
    if request.method == "GET":
        images = []
        if request.GET.get("images"):
            images_id = request.GET.get('images').split(",")
            for image_id in images_id:
                image = cache.get(image_id)
                images.append(image)
                cache.delete(image_id)

        return render(request, "home.html", {"form": form, "images": images})

    """Here we will handle the page requested by the user with prompt."""
    if request.method == "POST":
        prompt = request.POST.get("prompt")  # extracting the user's prompt
        search_prompt = SearchPrompt.objects.create(search_prompt=prompt)  # adding the prompt to database so that we have a record history

        """Here are 3 celery working extracting images parallaly through API as requested!"""
        image_url1_id = generate_images.delay(prompt, search_prompt.id)  # celery worker 1
        image_url2_id = generate_images.delay(prompt, search_prompt.id)  # celery worker 2
        image_url3_id = generate_images.delay(prompt, search_prompt.id)  # celery worker 3
        # Getting the generated images

        return render(request, "home.html", {"form": form, "images": [str(image_url1_id), str(image_url2_id), str(image_url3_id)]})


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
