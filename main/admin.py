from django.contrib import admin
from .models import ImageRepository, Image

# Register your models here.
admin.site.register(ImageRepository)
admin.site.register(Image)