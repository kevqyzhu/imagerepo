from django.forms import ModelForm
from .models import Image

class uploadImage(ModelForm):
    class Meta:
        model = Image
        fields =['image', 'description']
