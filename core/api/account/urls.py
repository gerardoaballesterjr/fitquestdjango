from django import urls
from core.api.account import views

app_name = 'account'

urlpatterns = [
    urls.path('update', views.UpdateView.as_view(), name='update'),
    urls.path('delete', views.DeleteView.as_view(), name='delete'),
    urls.path('password-change', views.PasswordChangeView.as_view(), name='password-change'),
]