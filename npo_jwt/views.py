from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from npo_jwt.serializers import RegisterSerializer, NPOObtainPairSerializer, UserFilterSerializer
from npo_user.models import NPOUser


class NPOObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = NPOObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = NPOUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class UserFilterSearchView(viewsets.ModelViewSet):
    queryset = NPOUser.objects.all()
    serializer_class = UserFilterSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['username', 'email']
    search_fields = ['=username', '=email']
    ordering_fields = ['username']
    ordering = ['username']
