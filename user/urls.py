
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path

# Your views (add them accordingly)
from .views import AdminView, ManagerView, UserView

# Set up Swagger/OpenAPI schema view
schema_view = get_schema_view(
   openapi.Info(
      title="API Documentation",
      default_version='v1',
      description="API documentation for the Rapid Labs project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@rapidlabs.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

# Define your API URL patterns
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/admin/', AdminView.as_view(), name='admin'),
    path('api/manager/', ManagerView.as_view(), name='manager'),
    path('api/user/', UserView.as_view(), name='user'),
    
    # Add Swagger or Redoc views
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),
]
