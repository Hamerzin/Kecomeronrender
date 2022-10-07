from rest_framework import serializers
from .models import RecipesModel

class RecipesSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecipesModel
        fields=["title","category","timeday","ingredients","number_of_dishes","category","link_video","image","description","recipes_time"]
