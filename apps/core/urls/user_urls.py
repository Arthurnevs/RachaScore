from django.urls import re_path
from apps.core.views.user_view import view_register_user

urlpatterns = [
    re_path(r"^register/$", view_register_user),
]
