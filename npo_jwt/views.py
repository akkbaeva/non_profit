from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from npo_jwt.serializers import RegisterSerializer, NPOObtainPairSerializer
from npo_user.models import NPOUser


class NPOObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = NPOObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = NPOUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
