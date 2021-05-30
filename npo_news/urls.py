from django.urls import path, include
from rest_framework import routers

from npo_news import views
from npo_news.views import NewFavoriteAPIView

router = routers.DefaultRouter()
router.register(r'', views.NewFilterSearchView, 'filter-news')

urlpatterns = [
    path('api/v1/news/', views.NewAPIView.as_view()),
    path('api/v1/news/<int:id>/', views.NewDetailAPIView.as_view()),
    path('api/v1/saved/', NewFavoriteAPIView.as_view()),
    path('api/v1/filter-news/', include(router.urls)),
]