from django.urls import path

from npo_news import views
from npo_news.views import NewFavoriteAPIView

urlpatterns = [
    path('api/v1/news/', views.NewAPIView.as_view()),
    path('api/v1/news/<int:id>/', views.NewDetailAPIView.as_view()),
    path('api/v1/saved/', NewFavoriteAPIView.as_view()),
]