from django.contrib.postgres.fields import JSONField
from django.db import models
import uuid
# Create your models here.

#
class UserEntity(models.Model):
    email = models.EmailField(null=False,unique=True,db_index=True)
    public_key = models.UUIDField("publicKey")
    private_key = models.UUIDField("privateKey",db_index=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.public_key = uuid.uuid4().hex
        self.private_key = uuid.uuid4().hex
        super().save(force_insert,force_update,using,update_fields)

    @classmethod
    def is_present(cls,email):
        return cls.objects.filter(email=email).count() > 0

from datetime import datetime

class DataStore(models.Model):
    user = models.ForeignKey(UserEntity)
    data = JSONField()
    created_on = models.DateTimeField(auto_now_add=True)
