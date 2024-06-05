from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterAPIView, UserInfo, LogoutAPIView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    # path('update-user/', UpdateUserAPIView.as_view(), name='update_user'),
    path('user-info/', UserInfo.as_view(), name='user_info'),
    path('log-out/', LogoutAPIView.as_view(), name='log_out'),
]
