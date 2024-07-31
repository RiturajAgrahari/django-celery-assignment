from django import forms


class PromptForm(forms.Form):
    """Creating django form to get users prompt from the django templates!"""
    prompt = forms.CharField(label="Enter Prompt", max_length=100)