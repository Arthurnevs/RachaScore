import uuid

from apps.core.enums.user_status_enum import UserStatusEnum
from apps.core.models.base_entity.base_entity import BaseEntity
from django.db import models


class User(BaseEntity):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=250)
    email = models.EmailField()
    password = models.TextField()
    status = models.CharField(max_length=50, choices=UserStatusEnum.choices, default=UserStatusEnum.ACTIVE)
