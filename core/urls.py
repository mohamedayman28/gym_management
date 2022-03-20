# Django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Django
    path('admin/', admin.site.urls),
    # Local apps
    path('', include('gym.urls')),
    # Third party:
    path('auth/', include('dj_rest_auth.urls')),  # Django rest framework.
    path('__debug__/', include('debug_toolbar.urls')),  # Django debug toolbar.
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
