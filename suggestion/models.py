from django.db import models
from uuid import uuid4


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        abstract = True


class City(BaseModel):
    name = models.CharField(max_length=500)
    latitude = models.FloatField(default=0.00)
    longitude = models.FloatField(default=0.00)

    def __str__(self):
        return self.name
