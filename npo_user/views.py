from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from npo_user.models import NPOUser
from npo_user.serializers import NPOUserSerializer


class RegisterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        user = NPOUser.objects.create(username=username,
                                      password=password,
                                      email=email,
                                      is_active=True)
        user.save()
        return Response(data=NPOUserSerializer(user).data,
                        status=status.HTTP_201_CREATED)

