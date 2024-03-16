from django import urls
from core.api.quest import views

app_name = 'quest'

urlpatterns = [
    urls.path('', views.IndexView.as_view(), name='index'),
    urls.path('<slug:slug>', views.DetailView.as_view(), name='detail'),
]