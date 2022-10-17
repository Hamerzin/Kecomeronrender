from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.views import APIView
from django.http import Http404
import json

from users.models import User
from users.serializers import UserCreationSerializer, UsersSerializers
from drf_yasg.utils import swagger_auto_schema
import requests
from django.contrib import messages
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.decorators import (api_view, permission_classes,
                                       renderer_classes)
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.shortcuts import redirect, render
from djoser.conf import django_settings
from django.urls import reverse


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
    #permission_classes = [IsAuthenticated]

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

    ##@api_view(['GET'])
    # PasswordResetView(request,uid,token):
    #    post_data = {'uid': uid, 'token': token}
    #    return Response(post_data)

from django.shortcuts import redirect, render
from djoser.conf import django_settings

@api_view(('GET', 'POST'))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@permission_classes([AllowAny])
def reset_user_password(request, **kwargs):
    # uses djoser to reset password
    if request.POST:
        current_site = Site.objects.get_current()
        #names of the inputs in the password reset form
        password = request.POST.get('new_password')
        password_confirmation = request.POST.get('password_confirm')
        #data to accept. the uid and token is obtained as keyword arguments in the url
        payload = json.dumps({
                'uid': kwargs.get('uid'),
                'token': kwargs.get('token'),
                'new_password': password,
                're_new_password': password_confirmation,
            })

        djoser_password_reset_url = '/api/v1/users/reset_password_confirm/'
        protocol = 'https'
        headers = {'content-Type': 'application/json'}
        if bool(request) and not request.is_secure():
            protocol = 'http'
        url = '{0}://{1}/{2}'.format(protocol, current_site,
                                     djoser_password_reset_url)
        response = requests.post(url,
                                 data=payload,
                                 headers=headers)

        if response.status_code == 204:
            # Give some feedback to the user.
            messages.success(request,
                             'Your password has been reset successfully!')
            return HttpResponseRedirect('/')
        else:
            response_object = response.json()
            response_object_keys = response_object.keys()
            #catch any errors
            for key in response_object_keys:
                decoded_string = response_object.get(key)[0].replace("'", "\'")
                messages.error(request, f'{decoded_string}')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
      # if the request method is a GET request, provide the template to show. in most cases, the password reset form.
    else:
        return render(request, 'pass_reset.html')
    
