from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('listings/', include('listings.urls')),
    path('realtor-api/', include('realtors.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
