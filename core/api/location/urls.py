from django import urls
from core.api.location import views

app_name = 'location'

urlpatterns = [
    urls.path('create', views.CreateView.as_view(), name='create'),
]