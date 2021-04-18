from django.contrib import admin
from django.urls import path, include
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi
from rest_framework import permissions

schema_view = get_schema_view(
      openapi.Info(
         title="Blog",
         default_version='v1',
         description="API for blog",
      ),
      public=True,
      permission_classes=(permissions.AllowAny,),
   )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include('chinook.urls')),
]
