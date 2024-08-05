from django import forms


class PromptForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control d-flex flex-column align-items-center justify-content-center'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    """Creating django form to get users prompt from the django templates!"""
    prompt = forms.CharField(label="Enter Prompt", max_length=100)