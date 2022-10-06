from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import RecipesModel
from .serializer import RecipesSerializer
from django_filters.rest_framework import DjangoFilterBackend

class RecipesViewset(ModelViewSet):
    serializer_class=RecipesSerializer
    queryset=RecipesModel.objects.all()
    
        
