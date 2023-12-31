from .views import RegisterAPI
from django.urls import path, include
from knox import views as knox_views
from .views import LoginAPI
from django.urls import path
from .views import ChangePasswordView, CoordinateAPI

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api/coordinate/', CoordinateAPI.as_view(), name='coordinate'),
]