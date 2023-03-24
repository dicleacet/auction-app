from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts import views

app_name = 'accounts'


router = DefaultRouter()

# Manager
router.register('users', views.UserViewSet, basename='manager_user')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserObtainTokenPairView.as_view(), name='login'),
    path('login/refresh/', views.UserTokenRefreshView.as_view(), name='login_refresh'),
    path('get-data/', views.UserGetDataView.as_view(), name='get_data'),
    path('password-forget/', views.PasswordResetEmailApiView.as_view(), name='password_forget'),
    path('password-reset/', views.PasswordResetApiView.as_view(), name='password_reset')
]

