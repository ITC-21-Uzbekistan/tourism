from django.db import models

from auth_user.models import User


class AbstractCLass(models.Model):
    is_delete = models.BooleanField(default=False)
    # deleted_by = models.IntegerField(null=True, blank=True)
    # created_by = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


