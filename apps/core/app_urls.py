from django.urls import include, re_path

urlpatterns = [
    re_path(r"^user/", include("apps.core.urls.user_urls")),
]
