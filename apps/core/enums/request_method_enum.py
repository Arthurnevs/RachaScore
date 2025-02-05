from django.db import models


class RequestMethodEnum(models.TextChoices):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
