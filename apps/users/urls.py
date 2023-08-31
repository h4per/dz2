from rest_framework.routers import DefaultRouter
from apps.users.views import UserAPIViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path


router = DefaultRouter()
router.register('users', UserAPIViewSet, 'api_users')

urlpatterns = router.urls

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="api_login"),
    path('refresh/', TokenRefreshView.as_view(), name="api_refresh"),
]

urlpatterns += router.urls