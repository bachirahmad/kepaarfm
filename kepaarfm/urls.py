from django.contrib import admin # type: ignore
from django.urls import path, include # pyright: ignore[reportMissingModuleSource]
from django.conf import settings # type: ignore
from django.conf.urls.static import static # pyright: ignore[reportMissingModuleSource]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('emissions/', include('emissions.urls')),
    path('actualites/', include('actualites.urls')),
    path('programmes/', include('programmes.urls')),
    path('animateurs/', include('animateurs.urls')),
    path('dons/', include('dons.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)