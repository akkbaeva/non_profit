from django.urls import path, include
from rest_framework import routers

from npo_publication import views

router = routers.DefaultRouter()
router.register(r'', views.PublicationFilterSearchView, 'filter-pub')

urlpatterns = [
    path('api/v1/pub/', views.PublicationAPIView.as_view()),
    path('api/v1/pub/<int:id>/', views.PublicationDetailAPIView.as_view()),
    path('api/v1/checkbox/', views.PublicationFavoriteAPIView.as_view()),
    path('api/v1/filter-pub/', include(router.urls)),
]