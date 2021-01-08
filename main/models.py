from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ImageRepository(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="imagerepository", null=True)

    def __str__(self):
        return self.name

class Image(models.Model):
    imageRepo = models.ForeignKey(ImageRepository, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.description

