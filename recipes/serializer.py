from rest_framework import serializers
from .models import Ingredients, RecipesModel



#class IngredientsSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model=Ingredients
   #     fields='__all__'


class RecipesSerializer(serializers.ModelSerializer):
    #ingredients=IngredientsSerializer(many=True, read_only=True)
    
    class Meta:
        model=RecipesModel
        fields=["title","category","timeday","ingredients","number_of_dishes","category","link_video","image","description","recipes_time"]
