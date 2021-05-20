from django.urls import path

from npo_publication import views

urlpatterns = [
    path('api/v1/pub/', views.PublicationAPIView.as_view()),
    path('api/v1/pub/<int:id>/', views.PublicationDetailAPIView.as_view()),
]