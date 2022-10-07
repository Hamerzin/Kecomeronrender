from django.urls import path
from recipes.routers import router
from recipes.genericviews import RecipesSearch

urlpatterns = [
    path('filter/', RecipesSearch.as_view()),
]
urlpatterns += router.urls