from django.db import models


class UserStatusEnum(models.TextChoices):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    REMOVED = "REMOVED"
