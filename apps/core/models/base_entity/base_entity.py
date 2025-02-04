from django.db import models
from django.db.models import Q


class BaseEntity(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @classmethod
    def is_empty(cls, query: Q) -> bool:
        return cls.objects.only("pk").filter(query).count() == 0

    @classmethod
    def is_not_empty(cls, query: Q) -> bool:
        return not cls.is_empty(query)
