from django.urls import path

from npo_user import views

urlpatterns = [
    path('api/v1/register/', views.RegisterAPIView.as_view()),
    path('api/v1/login/', views.LoginAPIView.as_view())
]