from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from npo_jwt import views
from npo_jwt.views import NPOObtainTokenPairView

urlpatterns = [
    path('api/v2/register/', views.RegisterView.as_view(), name='auth_register'),
    path('api/v2/login/', NPOObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('api/v2/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v2/token-verify/', TokenVerifyView.as_view(), name='token_verify'),
]