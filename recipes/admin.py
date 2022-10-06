from recipes.models import RecipesModel, Ingredients, Favorites
from django.contrib import admin



@admin.register(RecipesModel)
class RecipesAdmin(admin.ModelAdmin):
    list_display= ['id','title','category','timeday']


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display= ['id','dishe_1','dishe_2','dishe_3','dishe_4']

@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display= ['id','platillo','ingredientes']
