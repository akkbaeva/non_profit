from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect

# Create your views here.
from rest_framework import status
from rest_framework.authtoken.models import Token
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


# class LoginAPIView(APIView):
#
#     def login(self, request, *args, **kwargs):
#         if request.method == "POST":
#             form = AuthenticationForm(request, data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get('username')
#                 password = form.cleaned_data.get('password')
#                 user = authenticate(username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     messages.info(request, f"You are now logged in as {username}.")
#                     return redirect("main:homepage")
#                 else:
#                     messages.error(request, "Invalid username or password.")
#             else:
#                 messages.error(request, "Invalid username or password.")
#         form = AuthenticationForm()
#         return Response(data=NPOUserSerializer(form).data,
#                         status=status.HTTP_202_ACCEPTED)


class LoginAPIView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'],
                            email=request.data['email'],
                            password=request.data['password'])
        if not user:
            return Response(status=status.HTTP_404_NOT_FOUND,
                            data={'message': 'User not found or does not exist'})
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return Response(data={'token': token.key},
                            status=status.HTTP_200_OK)
