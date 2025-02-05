from django.contrib import admin
from django.urls import include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Meu Projeto API",
        default_version="v1",
        description="Documentação da API do meu projeto",
        terms_of_service="https://www.meusite.com/termos/",
        contact=openapi.Contact(email="contato@meusite.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path(r"^core/", include("apps.core.app_urls")),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
