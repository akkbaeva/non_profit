from django.urls import path, include
from rest_framework import routers

from npo_law import views

router = routers.DefaultRouter()
router.register(r'', views.LawFilterSearchSerializer, 'filter-law')

urlpatterns = [
    path('api/v1/law/', views.NPOLawAPIView.as_view()),
    path('api/v1/law/<int:id>/', views.NPOLawDetailAPIView.as_view()),
    path('api/v1/favorite/', views.LawFavoriteAPIView.as_view()),
    path('api/v1/filter-law/', include(router.urls)),
]