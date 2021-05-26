from django.urls import path

from npo_consultation import views

urlpatterns = [
    path('api/v1/questions/', views.QuestionAPIView.as_view()),
]