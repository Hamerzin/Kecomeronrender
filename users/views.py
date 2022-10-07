from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from django.http import Http404

from users.models import User
from users.serializers import UserCreationSerializer, UsersSerializers
from drf_yasg.utils import swagger_auto_schema


class UserCreateView(GenericAPIView):

    serializer_class = UserCreationSerializer

    @swagger_auto_schema(operation_summary="Create user", operation_description="This endpoint creates a users")
    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    @swagger_auto_schema(operation_summary="List user id", operation_description="This endpoint list a user")
    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = UsersSerializers(post)
        return Response(serializer.data)

    @swagger_auto_schema(operation_summary="Update user", operation_description="This endpoint update a user")
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = UsersSerializers(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


