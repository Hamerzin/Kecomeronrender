from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import RecipesModel
from .serializer import RecipesSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics


class RecipesViewset(ModelViewSet):
    serializer_class=RecipesSerializer
    queryset=RecipesModel.objects.all()

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="List Product", operation_description="This endpoint list a users")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RecipesSearch(generics.ListAPIView):
    queryset = RecipesModel.objects.all()
    serializer_class = RecipesSerializer

    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary="List user", operation_description="This endpoint list a users")
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)