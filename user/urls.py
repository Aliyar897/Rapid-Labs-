from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView # type: ignore
from .views import (
    AdminView,
    ManagerView,
    UserView,
)
urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/admin/', AdminView.as_view(), name='admin'),
    path('api/manager/', ManagerView.as_view(), name='manager'),
    path('api/user/', UserView.as_view(), name='user'),
]
