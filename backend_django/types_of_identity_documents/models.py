from django.db import models
from areas.models import UnsignedAutoField

class TypesOfIdentityDocuments(models.Model):

    id = UnsignedAutoField(
        unique=True,
        primary_key=True
    )

    code = models.CharField(max_length=5)

    description = models.CharField(max_length=200)

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date and time when the register was created"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Date and time when the register was updated"
    )
