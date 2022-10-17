from rest_framework import serializers
from .models import RecipesModel, Ingredients


class IngredientsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredients
        fields = ["dishe_1", "dishe_2", "dishe_3", "dishe_4", "dishe_5"]


class RecipesSerializer(serializers.ModelSerializer):
    ingredients = IngredientsSerializer()

    class Meta:
        model = RecipesModel
        fields = ["title", "link_video", "image", "category", "timeday", "like", "description","ingredients"]