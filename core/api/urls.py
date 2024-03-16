from django import urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

app_name = 'api'

urlpatterns = [
    urls.path('auth/', urls.include('core.api.auth.urls')),
    urls.path('account/', urls.include('core.api.account.urls')),
    urls.path('quest/', urls.include('core.api.quest.urls')),
    urls.path('location/', urls.include('core.api.location.urls')),
    urls.path('schema/', SpectacularAPIView.as_view(), name='schema'),
    urls.path('docs/', SpectacularSwaggerView.as_view(url_name='api:schema')),
]