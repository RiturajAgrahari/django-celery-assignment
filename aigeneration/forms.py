from django import forms


class PromptForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control d-flex flex-row align-items-center justify-content-center mb-2'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    """Creating django form to get users prompt from the django templates!"""
    prompt1 = forms.CharField(label="Enter First Prompt", max_length=100)
    prompt2 = forms.CharField(label="Enter Second Prompt", max_length=100)
    prompt3 = forms.CharField(label="Enter Third Prompt", max_length=100)