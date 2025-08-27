from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from .views import AlbumViewSet, PlayerViewSet, SongViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Music API",
      default_version='v1',
      description="Простой пример, как минимальный тест на профпригодность.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="i_kaukin@mail.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'albums', AlbumViewSet)
router.register(r'players', PlayerViewSet)
router.register(r'songs', SongViewSet)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/', include(router.urls)),
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += staticfiles_urlpatterns()
