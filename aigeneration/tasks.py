from celery import shared_task
from django.core.files.base import ContentFile
from .models import GeneratedImage, SearchPrompt

import base64
import os
import requests
from dotenv import load_dotenv

load_dotenv()


@shared_task()
def generate_images(prompt):
    """Here we are handling the celery worker who are assigned to extract the images by the requested prompts"""

    search_prompt = SearchPrompt.objects.create(
        search_prompt=prompt)  # adding the prompt to database so that we have a record history

    # Configuring API credentials
    engine_id = "stable-diffusion-xl-1024-v1-0"
    api_host = os.getenv('API_HOST', 'https://api.stability.ai')
    api_key = os.getenv("STABILITY_API_KEY")

    # handling API key expiration or something like this
    if api_key is None:
        raise Exception("Missing Stability API key.")

    # Sending request to API
    response = requests.post(
        f"{api_host}/v1/generation/{engine_id}/text-to-image",
        headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        },
        json={
            "text_prompts": [
                {
                    "text": prompt
                }
            ],
            "cfg_scale": 7,
            "height": 1024,
            "width": 1024,
            "samples": 1,
            "steps": 30,
        },
    )

    # handling exceptions
    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    # adding images to the model with there associated prompts to maintain record history
    data = response.json()
    image_url = ""
    for i, image in enumerate(data["artifacts"]):
        data = ContentFile(base64.b64decode(image["base64"]), name='temp.png')
        obj = GeneratedImage.objects.create(search=search_prompt, image=data)

        """NOTE :"""
        # this code of line will work locally, specifically without DOCKER, (because we changed the dir  name to 'app' in docker)
        # image_url = str(obj.image.path).split("django-celery\\")[-1]

        # when working in docker
        image_url = str(obj.image.path).split("app/")[-1]

    # returning the image URL
    return image_url

