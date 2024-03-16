from django import urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    urls.path('api/', urls.include('core.api.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)