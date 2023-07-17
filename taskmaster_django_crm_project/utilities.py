from enum import Enum

from django.db import models


class TimestampMixin(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ChoicesMixin(Enum):
    @classmethod
    def choices(cls):
        return tuple((item.name, item.value) for item in cls)

    @classmethod
    def max_length(cls):
        return max(len(item.value) for item in cls)


