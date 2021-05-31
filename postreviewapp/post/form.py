from django import forms
from .models import postdb

class ImageForm(forms.ModelForm):
    class Meta:
        model=postdb
        fields=("post_img","post_caption")