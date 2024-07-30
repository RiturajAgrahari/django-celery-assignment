from django.db import models

# Create your models here.


class SearchPrompt(models.Model):
    search_prompt = models.CharField(verbose_name="search prompt", max_length=100, null=False)


class GeneratedImage(models.Model):
    search = models.ForeignKey(SearchPrompt, on_delete=models.CASCADE)
    image_url = models.URLField(verbose_name="image url", null=False)

