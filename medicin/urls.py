from django.conf.urls.static import static
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from django.contrib import admin
from django.urls import path, include
from medicin import settings
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


schema_view = get_schema_view(
    openapi.Info(
        title="Medicine API",
        default_version='v1',
        description="These APIs for Medicine LLC",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(url="https://t.me/iProgrammer_One"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # noqa
    authentication_classes=(JWTAuthentication,),  # noqa
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),  # noqa
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # noqa
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # noqa
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('main/', include('main.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)