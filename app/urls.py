from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'AUCTION PANEL'
admin.site.site_title = 'AUCTION PANEL'
admin.site.index_title = 'Yönetim Paneli'


def home_page(request):
    return HttpResponse('AUCTION API')


urlpatterns = [
    path('', home_page, name='home'),

    # Api Urls
    path('api/accounts/', include('accounts.urls')),

    # ADMIN
    path('mgmt/', admin.site.urls),
    # PATTERNS
    path('api/schema/', login_required(SpectacularAPIView.as_view()), name='schema'),
    # Optional UI:
    path('swagger/', login_required(SpectacularSwaggerView.as_view(url_name='schema')), name='swagger-ui'),
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
