from django.urls import path

from npo_icnl import views

urlpatterns = [
    path('api/v1/icnl/', views.ICNLAPIView.as_view(), name='icnl-view'),
    path('api/v1/icnl/<int:id>/', views.ICNLDetailAPIView.as_view(), name='icnl-detail-view'),
    path('api/v1/saved2/', views.ICNLFavoriteAPIView.as_view(), name='icnl-favorite'),
]