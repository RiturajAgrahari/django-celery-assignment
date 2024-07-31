from django.contrib import admin
from .models import GeneratedImage, SearchPrompt

# Register your models here.

admin.site.register(GeneratedImage)
admin.site.register(SearchPrompt)