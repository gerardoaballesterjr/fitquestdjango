from django import urls
from core.api.auth import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'auth'

urlpatterns = [
    urls.path('register', views.RegisterView.as_view(), name='register'),
    urls.path('login', views.LoginView.as_view(), name='login'),
    urls.path('refresh', TokenRefreshView.as_view(), name='refresh'),
]