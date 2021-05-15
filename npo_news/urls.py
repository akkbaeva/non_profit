from django.urls import path
from npo_news import views

urlpatterns = [
    path('api/v1/news/', views.NewAPIView.as_view()),
    path('api/v1/news/', views.NewDetailAPIView.as_view()),

]