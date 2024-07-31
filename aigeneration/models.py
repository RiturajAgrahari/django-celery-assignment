from django.db import models

# Create your models here.


class SearchPrompt(models.Model):
    """Model to store user's searched prompts"""
    search_prompt = models.CharField(verbose_name="search prompt", max_length=100, null=False)


class GeneratedImage(models.Model):
    """Model to store images associated with the prompts"""
    search = models.ForeignKey(SearchPrompt, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="image", null=False, upload_to="media")

