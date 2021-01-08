from rest_framework import serializers
from .models import ImageRepository, Image

class ImageRepositorySerializer(serializers.ModelSerializer):
  class Meta:
    model = ImageRepository
    fields = ('user', 'name')

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields =['image', 'description']