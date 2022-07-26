from django.db import models
from django.utils import timezone


class AccountRole(models.Model):
    name = models.CharField(max_length=32)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name