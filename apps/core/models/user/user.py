import uuid

from django.db.models import Q

from apps.core.enums.user_status_enum import UserStatusEnum
from apps.core.models.base_entity.base_entity import BaseEntity
from django.db import models

from apps.core.utils.util import normalize_email


class User(BaseEntity):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.TextField()
    status = models.CharField(max_length=50, choices=UserStatusEnum.choices, default=UserStatusEnum.ACTIVE)

    def save(self, *args, **kwargs):
        self.email = normalize_email(self.email)

        query = Q(email=self.email)
        user_exists = User.objects.filter(query).exists()

        if user_exists:
            raise BaseException("Email not unique")

        super(User, self).save(*args, **kwargs)
